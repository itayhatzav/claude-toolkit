---
name: change
description: Plan, build and check any change to code, tools or shared config. Use when Itay asks to build, fix, change or add something with a code or tool surface. SKIP typos, one-line doc edits and work with no code or tool surface.
---
One flow, in the thread. Small and reversible: steps 1 and 5 in place, then `verify`, and say what you did.

1. **Look first.** Read the files involved. Before writing anything new, check in order and stop at the first that holds: this repo (grep), the standard library or a platform feature, an installed dependency, then GitHub prior art (what each did, what to borrow or avoid; "nobody built this" is earned by searching). Note dead ends (deprecated APIs, licence traps, closed routes). Say in plain English what is wrong and why it matters. Name the edge cases (empty, huge, concurrent, done twice, interrupted, stale state, permission denied) and whether each breaks loudly or silently: silent breakage is the finding.
2. **Gate check.** Does it touch a gate in the core's Gates list? Unsure: treat it as one. If yes, name the gate and stop there for his yes.
3. **Plan in chat, in Hebrew** (hebrew-text). A few lines for small work; for anything bigger, follow [plan.md](plan.md). Every public text in full.
4. **Review.** Anything beyond small and reversible: launch `reviewer` with the plan only; it pulls out the claims itself. Show the verdict and every finding in chat and answer each with FIX (what changed) or DISPUTE (`file:line` evidence). Re-run `reviewer` when a fix changes the approach. A finding that touches a decision Itay already made goes back to him. REJECT means plan again.
5. **Build** on a branch, the plan's minimum: no unrequested abstractions, options or files; remove what the change replaces. Needing more than the plan says is a stop-and-say, not a silent call. Mark each deliberate simplification with a `ceiling:` comment (limit and upgrade path). After touching startup or migration code, check the app still starts. Not a git repo: dated backups first (`cp f archive/f.bak-YYYY-MM-DD`). Hand the build to the `executor` agent only when it is wide and independent or a project skill says so; worktree isolation protects only this session's own repo, so start from a clean tree before delegating, then check its edits landed where intended (`git status`, and `git worktree list` if it ran isolated). Commit on the branch as part of finishing.
6. **Check** with the `qa-checker` agent: the plan's checks, each with a concrete expected value, run on the real output; pass it the project path, URL, database access and project type. On any fail, ask which rule let it through and propose the fix with `learn`.
7. **Hand over** with something to click, what to check and what good looks like, plus every `ceiling:` placed. Open the PR. Merge it yourself once review and QA pass and no gate is touched; otherwise wait for his yes.

Plans live in chat, not files.
