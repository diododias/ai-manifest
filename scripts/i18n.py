#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["Markdown>=3.7,<4"]
# ///
"""Translation tooling for the bilingual documentation.

The canonical tree lives at the repository root. Each target locale mirrors the
same paths under ``i18n/<locale>/``. A manifest records which version of the
canonical file each translation was made from, so drift is measurable instead of
being discovered by a reader.

Usage:
    uv run scripts/i18n.py status                 # report per file: current / outdated / missing
    uv run scripts/i18n.py status --porcelain     # one line per file, for sensors and CI
    uv run scripts/i18n.py stamp <path>...        # after translating, record the source version
    uv run scripts/i18n.py adopt --from <ref>     # import translations that live on another git ref

`status` is a sensor: it reports and exits 0. Use ``--strict`` to make it fail.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# The language the canonical tree at the repository root is written in. Flipping
# the direction of the whole project is a one-line change here plus a rename of
# the i18n/<locale> directory.
SOURCE_LOCALE = "en"
TARGET_LOCALES = ["pt-BR"]

CURRENT, OUTDATED, MISSING, ORPHAN = "current", "outdated", "missing", "orphan"


def corpus() -> list[str]:
    """The documents that must exist in every locale.

    Read from the site builder so the published corpus and the translated corpus
    can never disagree.
    """
    spec = importlib.util.spec_from_file_location("_site", ROOT / "scripts" / "build-docs-site.py")
    if spec is None or spec.loader is None:  # pragma: no cover - defensive
        raise SystemExit("cannot load scripts/build-docs-site.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return [item["path"] for item in module.PAGES]


def digest(text: str) -> str:
    """Hash the content, ignoring line-ending and trailing-whitespace noise."""
    normalized = "\n".join(line.rstrip() for line in text.replace("\r\n", "\n").split("\n")).strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def manifest_path(locale: str) -> Path:
    return I18N / locale / "_manifest.json"


def load_manifest(locale: str) -> dict:
    path = manifest_path(locale)
    if not path.is_file():
        return {"locale": locale, "source_locale": SOURCE_LOCALE, "entries": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(locale: str, manifest: dict) -> None:
    manifest["entries"] = dict(sorted(manifest["entries"].items()))
    path = manifest_path(locale)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def translated_path(locale: str, path: str) -> Path:
    return I18N / locale / path


def resolve(locale: str, path: str) -> tuple[Path, bool]:
    """Return the file to publish for this locale and whether it is translated."""
    candidate = translated_path(locale, path)
    if locale != SOURCE_LOCALE and candidate.is_file():
        return candidate, True
    return ROOT / path, locale == SOURCE_LOCALE


def state_of(locale: str, path: str, manifest: dict) -> str:
    source = ROOT / path
    target = translated_path(locale, path)
    if not target.is_file():
        return MISSING
    if not source.is_file():
        return ORPHAN
    recorded = manifest["entries"].get(path, {}).get("source_sha256")
    return CURRENT if recorded == digest(source.read_text(encoding="utf-8")) else OUTDATED


def report(locale: str) -> list[tuple[str, str]]:
    manifest = load_manifest(locale)
    paths = corpus()
    rows = [(path, state_of(locale, path, manifest)) for path in paths]
    known = set(paths)
    for extra in sorted(manifest["entries"]):
        if extra not in known:
            rows.append((extra, ORPHAN))
    return rows


def git_show(ref: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return result.stdout if result.returncode == 0 else None


def cmd_status(args: argparse.Namespace) -> int:
    worst = 0
    for locale in args.locales:
        rows = report(locale)
        counts = {CURRENT: 0, OUTDATED: 0, MISSING: 0, ORPHAN: 0}
        for _, state in rows:
            counts[state] += 1

        if args.porcelain:
            for path, state in rows:
                print(f"{state}\t{locale}\t{path}")
        else:
            total = len(rows)
            done = counts[CURRENT]
            pct = round(100 * done / total) if total else 0
            print(f"\n{locale}: {done}/{total} in sync ({pct}%)")
            print(
                f"  current {counts[CURRENT]}   outdated {counts[OUTDATED]}"
                f"   missing {counts[MISSING]}   orphan {counts[ORPHAN]}"
            )
            for label in (MISSING, OUTDATED, ORPHAN):
                listed = [path for path, state in rows if state == label]
                if listed and not args.summary:
                    print(f"\n  {label} ({len(listed)}):")
                    for path in listed:
                        print(f"    {path}")
        if counts[MISSING] or counts[OUTDATED] or counts[ORPHAN]:
            worst = 1

    return worst if args.strict else 0


def cmd_stamp(args: argparse.Namespace) -> int:
    locale = args.locale
    manifest = load_manifest(locale)
    stamped = 0
    for path in args.paths:
        path = Path(path).resolve().relative_to(ROOT).as_posix() if Path(path).is_absolute() else path
        path = path.removeprefix(f"i18n/{locale}/")
        source = ROOT / path
        if not source.is_file():
            print(f"skip (no canonical source): {path}", file=sys.stderr)
            continue
        if not translated_path(locale, path).is_file():
            print(f"skip (no translation): {path}", file=sys.stderr)
            continue
        manifest["entries"][path] = {"source_sha256": digest(source.read_text(encoding="utf-8"))}
        stamped += 1
    save_manifest(locale, manifest)
    print(f"stamped {stamped} file(s) for {locale}")
    return 0


def cmd_adopt(args: argparse.Namespace) -> int:
    """Import translations that already exist on another git ref.

    ``--from`` is the ref holding the translated text; ``--source-ref`` is the
    canonical version that text was translated from, which becomes the stamp.
    Files whose text on the ref is identical to the current canonical text are
    not translations at all and are left as missing.
    """
    locale = args.locale
    manifest = load_manifest(locale)
    adopted = skipped = identical = 0

    for path in corpus():
        source = ROOT / path
        if not source.is_file():
            continue
        content = git_show(args.from_ref, path)
        if content is None:
            for old, new in (pair.split("=", 1) for pair in args.rename):
                if path.startswith(new):
                    content = git_show(args.from_ref, path.replace(new, old, 1))
                    if content is not None:
                        break
        if content is None:
            skipped += 1
            continue
        if digest(content) == digest(source.read_text(encoding="utf-8")):
            identical += 1
            continue

        target = translated_path(locale, path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

        stamp_text = git_show(args.source_ref, path) if args.source_ref else None
        manifest["entries"][path] = {
            "source_sha256": digest(stamp_text) if stamp_text else "",
            "origin": args.from_ref,
        }
        adopted += 1

    save_manifest(locale, manifest)
    print(
        f"adopted {adopted} file(s) into i18n/{locale}/"
        f"  (not on ref: {skipped}, untranslated on ref: {identical})"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    status = sub.add_parser("status", help="report translation drift per file")
    status.add_argument("--locale", dest="locales", action="append", choices=TARGET_LOCALES)
    status.add_argument("--porcelain", action="store_true", help="machine-readable output")
    status.add_argument("--summary", action="store_true", help="counts only, no file list")
    status.add_argument("--strict", action="store_true", help="exit 1 when anything is out of sync")
    status.set_defaults(func=cmd_status)

    stamp = sub.add_parser("stamp", help="record the canonical version a translation was made from")
    stamp.add_argument("paths", nargs="+")
    stamp.add_argument("--locale", default=TARGET_LOCALES[0], choices=TARGET_LOCALES)
    stamp.set_defaults(func=cmd_stamp)

    adopt = sub.add_parser("adopt", help="import translations from another git ref")
    adopt.add_argument("--from", dest="from_ref", required=True, help="ref holding the translated text")
    adopt.add_argument("--source-ref", help="canonical ref that text was translated from (the stamp)")
    adopt.add_argument("--locale", default=TARGET_LOCALES[0], choices=TARGET_LOCALES)
    adopt.add_argument(
        "--rename",
        action="append",
        default=[],
        metavar="OLD=NEW",
        help="path prefix that moved since the translation was written",
    )
    adopt.set_defaults(func=cmd_adopt)

    args = parser.parse_args()
    if args.command == "status" and not args.locales:
        args.locales = TARGET_LOCALES
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
