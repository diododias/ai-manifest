# Local repositories

`repos/registry.yaml` records the expected clones. The code is in `github/<organization>/<repository>/`; competing missions use `worktrees/<organization>/<repository>/<work-item>/`.

## Recommended flow

1. Confirm organization, repository and default branch in the registry.
2. Clone to `repos/github/` and read the instructions in the repository itself.
3. Check the Git status before creating a mission.
4. Create branch and worktree identified by Work Item.
5. Record the paths in the Work Item before changing code.
6. Remove the worktree only after preserving commits and evidence.

Checkouts are ignored by the `.gitignore` in this example. Never document SHA or checkout cleanliness as if they were permanent status; refer to Git directly.
