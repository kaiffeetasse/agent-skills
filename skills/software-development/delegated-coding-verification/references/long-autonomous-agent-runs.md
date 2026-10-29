# Long autonomous agent runs (Claude Code CLI): spec, rounds, and verifying the claims

Pattern that produced a real result on a multi-hour reverse-engineering task (2026-10-16). The same
shape applies to any coding agent you drive non-interactively.

## 1. One self-contained spec file per round

Write `TASK_<topic>.md` **in the project** and pass it as the prompt (`claude -p "$(cat TASK_X.md) …"`).
It must contain:

* **Already settled** — the facts the run must not re-derive, each with a file/address reference.
* **Open items** in priority order, each phrased as a concrete action.
* **Tools & paths** — analysis projects, helper scripts, venv paths, existing automation.
* **Acceptance criteria** — hard and checkable ("`cmp -l` empty and MD5s equal", "screenshot shows X").
* **Evidence rules** — every claim needs a byte/address/command; results go into a named status file
  (`STATUS.md` §NN) and a per-round evidence directory (`workNN/`).
* **Known dead ends** — list paths already proven fruitless, or the run will happily repeat them.
* **Forbidden zones** — originals, live data, other people's copies: agents otherwise "fix" production
  copies to make a test pass.
* Host limits — foreground command caps, background jobs that can be killed, blocked `setsid`/`nohup`,
  tight RAM (explicitly forbid a second heavy analysis in parallel) — so it plans small steps.

Launch (background + completion notification):

```bash
claude -p "$(cat TASK_<topic>.md)

Beginne jetzt und arbeite autonom, bis <Kriterium> erreicht ist. Schreibe am Ende '## §NN' in
STATUS.md und lege alle Beweise in workNN/ ab." \
  --output-format json --max-turns 300 --permission-mode acceptEdits \
  --allowedTools 'Read,Write,Edit,Bash,Glob,Grep,WebSearch,WebFetch' \
  > workNN/claude_runN.json 2> workNN/claude_runN.err
```

* Print mode emits its JSON result **only on exit** → monitor progress via the files it creates
  (`find . -newermt '-20 minutes' -type f`), not stdout.
* Wire MCP servers **before** launching (`claude mcp add <name> -s user -e KEY=VALUE -- <cmd>`,
  then `claude mcp list` → `✔ Connected`); a running session will not pick them up.
* When a run stops at a documented boundary, the next round's spec names the remaining acceptance
  criterion **plus** the newly discovered dead ends.
* Treat each round as bounded work: the run is allowed to stop at "documented boundary + honest open
  list" — that is a usable handover, not a failure.

## 2. Verify the result yourself — the summary is a claim, not evidence

Real observation: a run reported success; the numbers were genuine, but only re-checking against the
**original** artifacts established that. Always:

1. Re-run the run's own selftest/demo command yourself.
2. Hash the *original* inputs and compare with the values quoted in its evidence file (e.g. per-page
   MD5 of the app-written reference file).
3. Read the section where it says what is **not** solved — that is where the remaining acceptance
   criteria live; report those explicitly instead of relaying "done".
4. Keep the run's evidence directory intact as the audit trail.

"Agent says it works" ⇒ "agent says it works". Only an independent check turns it into a fact.

## 3. Read-only investigation rounds

For triage/analysis the run must not edit code. Pass the write tools away explicitly and give it one
output file:

```bash
claude -p "$(cat TRIAGE_TASK.md)" \
  --allowedTools "Read,Grep,Glob,Write,Bash" --disallowedTools "Edit" \
  --dangerously-skip-permissions --max-turns 150 --output-format text > .triage/run.log 2>&1
```

A per-item verdict table (`item | verdict | file:line evidence`) written to a file is the usable
artifact; the chat summary is not. Always re-read the two or three highest-stakes verdicts yourself —
in a bot-fed backlog a wrong `fixed` hides a live bug, and a wrong `unknown` costs the user a decision.

## 4. Parallel rounds: one worktree each, and set git identity first

Two runs in one clone race on the index and produce interleaved, unmergeable diffs. Give each round its
own tree:

```bash
git worktree add -q ../repo-wt-<ticket> -b fix/<ticket>
```

Worktrees share the repository config, but a fresh clone often has **no commit identity** — every run
then does all the work and fails only at `git commit` (`Please tell me who you are`). Set it once in the
main clone before launching:

```bash
git config user.name "<name>" && git config user.email "<email>"
```

Merge each tree back with `--ff-only` after rebasing onto the moved main, then `git worktree remove` it;
leave no stray trees behind.

## 5. The provider session/quota limit lands mid-run

Long rounds die on the CLI's own usage limit, not on the task: the log shows the limit banner, the tree
holds whatever the run managed to edit, and nothing is committed. Do not relaunch into the same wall —
read `git status`/`git diff`, finish the mechanical remainder yourself (a bulk rename, deleting unused
imports, re-running the suite), and commit with the real verification result. A run that stopped at a
quota is a handover, not evidence of anything about the code.

## 6. Hard gates belong in the spec, not in the launch line

When the repository has its own CI/QA automation, the spec file must carry the boundaries: never push,
never open a PR, one ticket per run, no opportunistic refactors, and the exact verification commands.
Those constraints survive the run's own context compaction; a flag on the command line does not.
