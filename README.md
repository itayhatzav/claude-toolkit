# claude-toolkit

Itay's personal Claude Code plugin. One install gives every project the same working method.

- `core/personal-core.md`: the ~60-line personal rulebook. It goes in Project instructions (a plugin cannot carry always-on rules).
- `skills/`: change, verify, debug, assess-idea, learn, new-project, hebrew-text.
- `agents/`: reviewer (Opus, fresh eyes), qa-checker (Sonnet).
- `hooks/hooks.json` + `hooks/guard.py`: a hard block on pushing to main, `git add -A` and force pushes.

Install: claude.ai > Customize > Plugins > Add marketplace (this private repo), or Project settings > Plugins for cloud threads.
Whether plugin hooks run inside cloud project threads is unverified; the test thread settles it. Until then the gates also rely on branch protection on main.

Credits: ideas borrowed from Alan Cohen's course (loop, lanes, gates), obra/superpowers (verify-before-done, systematic debugging) and github/spec-kit (idea assessment), all rewritten, none copied.
