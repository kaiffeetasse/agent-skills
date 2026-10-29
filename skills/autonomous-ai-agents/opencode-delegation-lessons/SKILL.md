---
name: opencode-delegation-lessons
description: "Use when delegating coding to OpenCode CLI via Hermes."
---

# OpenCode Delegation — Field Lessons

Companion to the bundled `opencode` skill (which documents commands/flags). This skill captures what actually went wrong and worked in real delegation sessions. Read it before starting any `opencode` background/TUI session.

## Core recommendation

**Prefer `opencode run '<task>'` for delegated coding tasks** — including multi-step tasks with commits and verification. It streams the final report to stdout and avoids every TUI failure mode listed below. Reserve the interactive TUI for genuinely iterative back-and-forth the user participates in.

## TUI failure modes observed (and fixes)

### 1. Prompt sits unsent in the input box
`process(action="submit", ...)` writes the text but often doesn't submit. Fix: follow with `process(action="write", data="\n")`. Sometimes even that fails silently — if the log shows no new session created after ~1 min, assume not submitted.

### 2. Invisible permission dialogs = silent hang
If the task references files OUTSIDE the workdir (e.g. a plan at `~/.hermes/plans/...`), opencode fires an `external_directory` permission ask. The TUI shows a spinner; nothing progresses for 10+ minutes.

**Fix:** Copy context files INTO the project first (`cp ~/.hermes/plans/x.md docs/plan.md && git add && git commit`), then reference them by relative path in the prompt. Tell the agent explicitly: "bleibe im Projektverzeichnis".

Diagnose with:
```bash
grep -E "asking|permission" $(ls -t ~/.local/share/opencode/log/*.log | head -1) | tail -5
```
(`permission=external_directory ... message=asking id=...` = this hang.)

### 3. Model IDs drift
An invalid model ID (`opencode/deepseek-v4-flash-free`) produces "Model is not valid" or silent stalls/fallbacks. Always verify first:

```bash
opencode models deepseek   # list provider's models
```

Working default as of 2026-08: `deepseek/deepseek-v4-flash` (direct DeepSeek provider).

### 4. Turn ended without work ("exiting loop")
Check newest log for `"exiting loop"`; then verify on disk (git log, generated files, cache dirs). If the turn ended without side effects, re-dispatch — don't wait longer.

### 4b. Long `opencode run` can die mid-deliverable (observed 2026-10-08)
A background `opencode run --auto ... | tee logs/run.log` on a multi-part task (decompile jar →
build → dual-mode E2E verify → report) processed part of the brief and then the process simply
disappeared: the log stopped mid-command at 11:39, `ps` showed nothing, no "exiting loop", and
several required outputs (screenshots, updated verify script, report update) were missing while
others (patcher edits to source files, a partial build script) were already on disk.

Fix / discipline:
- Treat the log tail as *not* proof of completion. Check every named deliverable on disk
  (`ls screenshots/`, `grep -c <section> docs/REPORT.md`, expected scripts present+executable).
- Expect a partially-applied change set; inspect the diff before re-dispatching so a second run
  doesn't undo work. Finishing the leftovers yourself is usually faster than a new agent round.
- Split large briefs into phases so each phase is a complete, independently checkable deliverable.

### 5. Input buffer corruption on kill/restart
Killing a stuck TUI can leave queued input garbled (`&#10;`, literal `\n` mixed into the prompt text). Don't try to salvage the buffer — kill the process and start fresh, resending the full task cleanly.

## Monitoring pattern that works

Watch progress via the **filesystem**, not the TUI spinner:

```bash
git -C <workdir> log --oneline | head -3        # commits landed?
find <workdir>/build/cache -name "*.png" | wc -l # long downloads progressing?
du -sh <dir>                                     # size growing?
tail -20 $(ls -t ~/.local/share/opencode/log/*.log | head -1)  # current activity
```

Long-running agent sub-tasks (tile downloads, builds) keep running while the agent turn is open — poll these counters every few minutes rather than killing prematurely.

## Verification discipline (orchestrator role)

Never trust the agent's self-report alone:
- Re-run its verification yourself (open generated files with PIL, check manifest counts against formulas, `node --check`).
- Do visual spot-checks of generated assets (stitch two neighbors side-by-side, screenshot the app headless) — the agent can be right about counts and wrong about rendering.
- Sanity-check the agent's math against your own plan numbers; in one real session the agent correctly caught an off-by-100 error in the orchestrator's plan (z13 tile estimate) — verify claims both ways.

## Related project

The full worked example (map-puzzle: OSM tile pipeline + puzzle web app, built entirely via opencode delegation) lives in `~/workspace/map-puzzle/` with its plan in `docs/plan.md` there.
