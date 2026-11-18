# claude-toolkit

Itay's personal Claude Code plugin. One install gives every project the same working method.

- `core/personal-core.md`: the ~60-line personal rulebook. It goes in Project instructions (a plugin cannot carry always-on rules).
- `skills/`: change, verify, debug, assess-idea, learn, new-project, hebrew-text.
- `agents/`: reviewer (Opus, fresh eyes), qa-checker (Sonnet).
- `hooks/hooks.json` + `hooks/guard.py`: a hard block on pushing to main, `git add -A`, force pushes, `git reset --hard`, `git clean -f` and `rm -rf` on the root, home or current folder.

Install: claude.ai > Customize > Plugins > Add marketplace (this private repo), or Project settings > Plugins for cloud threads.
Verified 2026-11-18: plugin hooks do run inside cloud project threads (a `git add` with the all-files flag was blocked there). Branch protection on main still backs the push rule. `python3 -I hooks/test_guard.py` checks the hook's patterns.

Credits: ideas borrowed from Alan Cohen's course (loop, lanes, gates), obra/superpowers (verify-before-done, systematic debugging) and github/spec-kit (idea assessment), all rewritten, none copied.
