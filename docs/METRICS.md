# Metrics

DORA measures delivery; it does not measure the harness. Autonomy requires evidence that the verification system catches what it claims to catch.

## Primary signal

**Gate escape rate** is the number of defects found after the gate that should have caught them, per accepted Work Item.

Segment it by detection point, severity and responsible gate. Attribute the escape to the control that failed, never to the person or agent that authored the change. Pipeline success reports what gates caught; escape rate reports what they missed.

## Supporting signals

- **Escalation rate:** a near-zero rate combined with rising escapes indicates silent guessing; a high rate alone is inconclusive.
- **Rework after merge:** accepted changes materially reopened or corrected within a fixed window.
- **Feedback latency by layer:** sensor, fast-lane and deep-lane latency measured separately.
- **Skip and degraded rate:** `skipped` gates, quarantines and retries ([Failure](FAILURE.md)).
- **Cost per accepted Work Item:** total agent, model and review cost across every attempt.
- **Evidence completeness:** accepted items that an independent reviewer can re-verify unaided.
- **Review latency and depth:** elapsed time to decision, paired with substantive review evidence.

Do not optimize any signal in isolation. Lower cost with higher rework, lower escalation with higher escapes, or faster review without review depth are regressions.

## Promotion and demotion

- **Promote** only when the required artifacts exist ([Maturity](MATURITY.md)) and the signals hold for a sustained window.
- **Demote** when escape or skip rates rise, evidence becomes stale, or escalation collapses without a corresponding reduction in ambiguity.

The ladder must move in both directions; otherwise it records history rather than current capability.

## Reject as control metrics

- Per-person or per-agent rankings.
- Commits, lines, pull requests, tokens or other volume proxies.
- Gate pass rate without canaries and escape attribution.

## Sources

`gate-status.json` provides gate states, `attestation.json` records the producing context, evidence packs contain verification output, and version-control history provides rework and review timing. Defect records must add the gate that should have caught the escape; without that field the panel measures activity, not verification.

---

*Next: [Maturity](MATURITY.md) — what each level requires, and how to find out where a repository actually stands.*
