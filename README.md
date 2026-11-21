# claude-toolkit

Itay's personal Claude Code plugin. One install gives every project the same working method.

- `core/personal-core.md`: the personal rulebook (about 50 lines), the single source of Itay's personal rules. A plugin cannot carry always-on rules, so it reaches sessions another way: on the Mac, `~/.claude/CLAUDE.md` loads it; in cloud environments, the setup script writes it to `~/.claude/CLAUDE.md` (pasting it into Project instructions is the fallback).
- `skills/`: change, verify, debug, assess-idea, learn, new-project, hebrew-text.
- `agents/`: reviewer (Opus, fresh eyes), qa-checker (Sonnet).
- `hooks/hooks.json` + `hooks/guard.py`: a hard block on pushing to main, `git add -A`, force pushes, `git reset --hard`, `git clean -f` and `rm -rf` on the root, home or current folder.

Install: claude.ai > Customize > Plugins > Add marketplace (this public repo; keep secrets and business details out of it), or Project settings > Plugins for cloud threads.
Verified 2026-11-18: plugin hooks do run inside cloud project threads (a `git add` with the all-files flag was blocked there). Branch protection on `main` also backs the push rule. The hook reads real commands (quoted text such as a commit message is not blocked); `python3 -I hooks/test_guard.py` runs 69 block/allow cases against it.

Credits: ideas borrowed from Alan Cohen's course (loop, lanes, gates), obra/superpowers (verify-before-done, systematic debugging) and github/spec-kit (idea assessment), all rewritten, none copied.
