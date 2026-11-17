---
name: change
description: Plan, build and check any change to code, tools or shared config. Use when Itay asks to build, fix, change or add something that touches files others depend on. Replaces the old investigate/plan/review/exec/qa chain with one flow and one independent review. SKIP for typos, one-line doc edits and anything with no code or tool surface.
---
One flow, in the thread, no separate agent per step.

1. **Look first.** Read the code or files involved. Check what already exists in the repo, then GitHub for prior art. Say in plain English what is wrong and why it matters. Name the edge cases (empty, huge, twice, interrupted, stale state) and whether each breaks loudly or silently.
2. **Gate check.** Does it touch a gate (money, public words, secrets, destructive, terms of service, merge)? If yes, say which gate and plan to stop there for his yes. Gates are never skipped by the flow.
3. **Plan in chat.** Short: what changes, what is removed, how it will be proven. Name the model and effort. Show every public text in full.
4. **Review.** For any change that touches a gate or shared tooling, launch the `reviewer` agent (fresh, Opus, high) with the plan. It verifies that named files and functions exist, that old code is removed, that the diff is minimal, and that the proof matches the claim. Answer every finding with FIX or DISPUTE. A finding that touches a decision Itay already made goes back to him.
5. **Build** on a branch. Build the minimum. Never commit unless asked.
6. **Check** with the `qa-checker` agent (Sonnet, high): a concrete expected value per check, run on the real output. On any fail, ask which rule let it through and propose the fix with `learn`.
7. **Hand over** with something to click, what to check and what good looks like.

Plans live in chat, not files. Small, reversible work needs only steps 1, 5 and 6.
