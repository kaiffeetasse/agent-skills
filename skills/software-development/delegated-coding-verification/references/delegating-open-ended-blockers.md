# Delegating an open-ended blocker to a coding agent

Most of this umbrella assumes the delegated unit is "apply this change". This file covers the harder
case: **the blocker is "figure out how X actually works"** — an unknown file format, one unexplained
byte, a spec that does not exist yet. Then the delegation must carry the *problem statement and the
proof burden*, not just a task. Pattern that was used successfully (Claude Code, print mode):

## 1. Write the task as a spec file in the workdir, pass it as the prompt

`TASK_<TOPIC>.md` next to the code, then `claude -p "$(cat TASK_<TOPIC>.md)"`. It must contain:

* **Goal** in one paragraph, plus what "done" means for the user.
* **Ground-truth artifacts** — reference files with *known* values (a small, app-generated reference
  beats a big real dataset), the existing tooling, and a pointer to the project status document.
* **Dead ends explicitly listed** ("do not repeat: the string-anchor approach was refuted here, the
  prototype scan gave a false positive") — a spec that lists prior failures is worth as much as one
  that lists requirements; without it the agent re-treads solved work.
* **Environment limits** of the host (e.g. foreground calls abort at ~420 s, background jobs can be
  reaped, detached runners are blocked) so the agent shapes its steps instead of losing runs.
* **Hard, machine-checkable acceptance criteria**: byte/hash equality against a reference (`cmp`),
  a named log marker, a screenshot path — never "looks correct".
* **Evidence rule**: every claim gets a byte/address/command citation, findings go into the status doc
  as a new section.

## 2. Give it the capabilities you already have

An MCP server configured for the orchestrator can be registered for another CLI — no need to let the
agent rebuild the capability:

```bash
claude mcp add rea -s user -e GHIDRA_INSTALL_DIR=<dir> -e SOME_TIMEOUT_MS=3600000 \
  -- npx -y <package> mcp
claude mcp list     # expect:  <name>: … - ✔ Connected
```

* `-e KEY=VALUE` passes environment variables; `-s user` stores them for all projects.
* A server registered **after** a delegated session started is **invisible to that session** — register
  first, then launch (or re-launch).
* Anything the server needs at runtime (engine paths, raised timeouts/heap) belongs in those env vars;
  defaults are usually sized for small inputs only.

## 3. Run and monitor it

* Tracked background job + `notify_on_complete`, print mode, caps:
  `-p … --max-turns 250 --permission-mode acceptEdits --allowedTools 'Read,Write,Edit,Bash,Glob,Grep,WebSearch,WebFetch'`,
  JSON result redirected into a run directory.
* Print mode emits its result only **at the end**, so read progress from the **working tree**
  (files created/changed since dispatch), not from stdout.
* **Pause your own automation on the same problem** (cron job, watcher) while the agent works — two
  writers on the same files produce contradictory evidence and corrupt each other's reference data.

## 4. Verify the self-report

Treat the child's summary as a claim. Check the acceptance criteria yourself (hash/`cmp` output, the
screenshot, the log line), read the section it added to the status doc, and confirm each citation
resolves. "Task complete" with no machine-checkable number is not a result — report the layer that is
proven, the layer that failed, and the layer that was not verified, separately.
