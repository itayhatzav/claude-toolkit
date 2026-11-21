---
name: now
description: Status snapshot of what is running right now, in at most 5 lines.
disable-model-invocation: true
effort: low
allowed-tools: mcp__ccd_session_mgmt__list_sessions
---
At most 5 lines, plain English, no headings, no narration.
1. Find what is still running: background agents you launched that haven't sent their completion notice; side sessions you started (`mcp__ccd_session_mgmt__list_sessions` with `{"linked": true}`, rows working or starting, where that tool exists); background shell commands that haven't reported.
2. Nothing running and you are not mid-step: print exactly `resting` and nothing else.
3. Otherwise one line for your own step (or "Waiting on agents"), then one line per worker: `<model> · <what, in a few words> · ETA <time>`. More than 4 workers: the 3 longest-running plus "+N more".
Never start, stop or message anything from here, and never guess a result: "running" is all you know until its notice arrives.
