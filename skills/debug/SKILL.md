---
name: debug
description: Find the root cause of a bug or surprising result before fixing it. Use when something is broken, wrong, flaky or "worked yesterday".
---
1. Reproduce it. Get the exact failing input and output. If it can't be reproduced, say so and stop guessing.
2. Narrow it: what changed since it last worked (git log, config, data)? Bisect rather than reading everything.
3. State the cause as a claim and test it with one cheap experiment that could prove it wrong. Do not fix from a hunch.
4. Fix the cause once, inside the shared function, not in each caller.
5. Re-run the reproduction, then the neighbours. Then ask which rule or check should have caught it, and propose it with `learn`.
Explain in plain English first: what broke, why it matters, then the technical detail.
