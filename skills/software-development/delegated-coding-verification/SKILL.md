---
name: delegated-coding-verification
description: "Use when delegating repository changes to coding agents."
version: 1.0.0
license: MIT
metadata:
  hermes:
    tags: [coding-agents, opencode, verification, orchestration]
---

# Delegated Coding Verification

## Purpose

Use this workflow when an external coding agent such as OpenCode is asked to modify a repository. The deliverable is verified repository changes, not merely a running agent or a claimed summary.

## Workflow

0. **Pick the model tier before slicing.** Planning, architecture and cross-cutting design go to the
   strongest model available (e.g. Opus at high effort); implementing one scoped slice goes to a
   mid-tier model (Sonnet); mechanical work — docs, test plans, formatting, small fixes, bulk edits —
   goes to the cheapest model or a `delegate_task` subagent. Do not spend the expensive tier on
   boilerplate, and do not downgrade a run that is already most of the way through: letting it finish
   is cheaper than redoing verified work. Apply the tier choice to the next slice instead.
1. Inspect the repository and identify the smallest coherent implementation slice.
2. Keep each delegated request narrow. Large source files are read into provider context, so free-tier request limits can be exceeded even when the user's visible prompt is short.
3. Split broad work into sequential slices, such as backend integration, data expansion, then end-to-end verification. Avoid one run for unrelated large changes.
4. Use an exact model identifier obtained from `opencode models`; display names are not necessarily valid CLI IDs.
5. Prefer `opencode run` for bounded work. If an interactive TUI remains at its prompt without acting, stop it and restart non-interactively rather than repeatedly submitting input.
6. After the agent exits, independently inspect changed files, timestamps/content, and actual test commands. An exit code, summary, or process liveness is not evidence that edits landed.
7. Run relevant project checks yourself when possible: typecheck, unit tests, build, then live/UI/API checks.
8. Report each layer separately as passed, failed, not verified, or not implemented. Do not claim real backend integration when credentials or a configured backend were unavailable.

## Common Pitfalls

- An agent can fail after reading the repository but before editing because the provider's effective request includes inspected context.
- A TUI can appear active while the request remains unsent in its input area.
- A coding agent can stop at its turn/token limit after editing but before committing. Treat the working tree as the source of truth: inspect `git status`/`git diff`, run the full tests yourself, commit or explicitly report the uncommitted state, and restart any long-running server before declaring the feature live. A printed “all tests pass” summary is not a commit.
- **A killed run is not a failed run — salvage it instead of re-dispatching.** When a background coding agent dies mid-flight (SIGTERM from a closed turn, timeout, provider drop) the tree usually holds most of the implementation and no commit and no build. Do not re-run the whole task: audit that tree against the spec's definition of done (which files it must touch, which branches/handlers must be wired — grep for the call site, not just the new helper), judge the diff yourself, then finish the remainder in your own session: lint the touched files, build the package, write the commit. Re-dispatching costs the full budget again and yields a *different* implementation, so any verification done so far is lost.
- A run can edit code, pass the tests, and still fail its own live proof: commands that write outside the repository (scratch DBs, `/tmp` scripts, downloaded artifacts) hit the sandbox's `external_directory` permission and are auto-rejected. The final summary then reports the code work but not the verification. Read the transcript tail for `permission requested` / `rejected`, and run every out-of-repo verification step yourself; keep delegated instructions inside the repo, or pre-create the scratch paths the run needs.
- A repository may lack Git metadata; use direct file inspection and test output rather than assuming `git diff` is available.
- A successful static build does not prove Supabase persistence, realtime delivery, or multi-session behavior.
- A delegated test can pass for the wrong reason. Read the test you were handed and ask what input makes it fail: a "recovers once the endpoint is up" case that starts the listener *before* calling the retry helper never enters the failure path and asserts one attempt — green, covering nothing. Rebuild it so attempt 1 genuinely fails and attempt 2 succeeds (replay the real captured error object), then confirm it goes red when the production change is reverted.
- Diff the control flow around the edit, not just the added lines. Agents restructure the block they touched: a `JSON.parse` lifted from inside the per-item `try` to just above it silently turns a logged-and-continued error into one that escapes the loop. Compare the before/after shape of every enclosing `try`/`catch`, early return and loop body.
- A run that ends with a question did no work. When the agent's final message asks for confirmation — typically after reading the repo's own contribution policy — its exit code is still 0 and the tree is untouched. Check `git status` before believing anything, then re-run with continuation plus an explicit "Yes, proceed: <what>", or take the policy question to the user if it is real.

## Related Skills

For long non-interactive runs (spec file, read-only triage rounds, parallel worktrees, provider session
limits, verifying the agent's claims) see `references/long-autonomous-agent-runs.md`.

This umbrella complements `opencode` for delegation mechanics and `web-app-e2e-verification` for independent live verification. Those skills may be bundled/protected; keep this umbrella focused on orchestration and evidence.
