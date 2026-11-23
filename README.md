# claude-toolkit

Itay's personal Claude Code plugin. One install gives every project the same working method.

- `core/personal-core.md`: the personal rulebook (about 50 lines), the single source of Itay's personal rules. A plugin cannot carry always-on rules, so it reaches sessions another way: on the Mac, `~/.claude/CLAUDE.md` loads it; in cloud Projects, it is pasted into Project instructions (tested 2026-11-22: the project chat never runs an environment setup script, so that route can't reach it).
- `skills/`: change (with plan.md), verify, debug, assess-idea, learn, capture, research, follow-run, hebrew-text, new-project, mac-handoff (briefs for sessions on Itay's computer), finish-task (the closing routine: verify, board, usage line, lesson, something to click); slash-only: now, explain.
- `agents/`: reviewer (Opus, high), qa-checker (Sonnet, high), executor (Sonnet, high), researcher (Sonnet, high; Opus for deep runs).
- `hooks/hooks.json` + `hooks/guard.py`: a hard block on pushing to main, `git add -A`, force pushes, `git reset --hard`, `git clean -f` and `rm -rf` on the root, home or current folder.

Install: claude.ai > Customize > Plugins > Add marketplace (this public repo; keep secrets and business details out of it), or Project settings > Plugins for cloud threads.
Verified 2026-11-18: plugin hooks do run inside cloud project threads (a `git add` with the all-files flag was blocked there). Branch protection on `main` also backs the push rule. The hook reads real commands (quoted text such as a commit message is not blocked); `python3 -I hooks/test_guard.py` runs 69 block/allow cases against it.

Credits: ideas borrowed from Alan Cohen's course (loop, gates), obra/superpowers (verify-before-done, systematic debugging) and github/spec-kit (idea assessment), all rewritten, none copied.
