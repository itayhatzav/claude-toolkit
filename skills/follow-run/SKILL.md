---
name: follow-run
description: Watch a long job (build, batch, render, deploy, background agent) and report unasked: ETA, progress, live output checks, stall alarm, end report. Use for "follow the run", "tell me when it's done", or any job over a few minutes.
argument-hint: "[log path, job id or what to follow]"
---
The system reports; Itay never has to ask "what now?".
1. **Find the signal**, in this order: a log file to tail, a read-only status endpoint or row to poll, or the process itself (`ps` plus output file times). Say which.
2. **ETA first**, from unit costs (items × seconds per item), assumptions stated. Can't estimate yet: say what the first unit will tell you, then give it.
3. **Poll in the background** (`run_in_background`, or the Monitor tool where present), never a foreground sleep loop (it dies at the 2-minute Bash timeout). Report on each stage change and at least every ~5 minutes: `stage · N/M done · ETA`. Say so unprompted the moment the ETA slips.
4. **Live checks:** as outputs land, check them against the project's rules and flag a problem at once, with the path.
5. **Stall watchdog:** no new output for about twice the per-unit time means stuck, not slow. Say so with the last known state and the recovery options.
6. **End report:** the result, each failure with its suspected cause, anything that should feed back into the plan or rules. Ping his phone.
Read-only toward the run: never kill, restart or change it; offer the options and let Itay or the owning session decide.
