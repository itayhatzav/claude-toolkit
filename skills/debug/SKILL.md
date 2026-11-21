---
name: debug
description: Find the root cause before fixing. Use when something is broken, wrong, flaky or "worked yesterday", or Itay asks to investigate, diagnose or why X does Y.
---
An exact tiny thing (a quoted typo, a named label): look, fix, say what you did. No ceremony.
1. Reproduce it. Get the exact failing input and output. If it can't be reproduced, say so and stop guessing.
2. Narrow it: what changed since it last worked (git log, config, data)? Bisect rather than reading everything.
3. State the cause as a claim and test it with one cheap experiment that could prove it wrong. Do not fix from a hunch.
4. Look next door: empty, huge, done twice, interrupted, stale state from the last run. Silent breakage is the finding.
5. Fix the cause once, inside the shared function, not in each caller. A fix bigger than small goes through `change`.
6. Re-run the reproduction, then the neighbours. Then ask which rule or check should have caught it, and propose it with `learn`.

Report, plain English first:
- **What's going on:** symptom vs cause and why it matters to users or the business. He can decide from this alone.
- **Evidence:** each claim with `file:line`, or the command and what it printed.
- **Fix:** the smallest correct one, what it removes, and any gate it touches.
