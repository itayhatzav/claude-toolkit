"""Checks hooks/guard.py: every dangerous command is blocked, every ordinary one passes.
Run: python3 -I hooks/test_guard.py"""
import json, os, subprocess, sys

GUARD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guard.py")
BLOCK = [
    "git push origin main", "git add -A", "git add .", "git push -f origin x",
    "git push --force origin x", "git reset --hard HEAD~1", "git clean -fd",
    "git clean -fdx", "rm -rf /", "rm -rf ~", "rm -rf $HOME", "rm -rf .",
    "rm -rf ..", "rm -rf *", "rm -fr /", "rm -r -f ~/", "rm -rf ./*",
]
PASS = [
    "git push --force-with-lease origin x", "git add CLAUDE.md", "git reset --soft HEAD~1",
    "git reset HEAD file", "git clean -n", "rm -rf build/", "rm -rf ../tmp-copy",
    "rm file.txt", "rm -r build", "git push origin claude/x", "rm -rf /tmp/x",
]


def blocked(cmd):
    out = subprocess.run([sys.executable, "-I", GUARD], input=json.dumps({"tool_input": {"command": cmd}}),
                         capture_output=True, text=True).stdout
    return "deny" in out


bad = [c for c in BLOCK if not blocked(c)] + [c for c in PASS if blocked(c)]
print("FAIL:" if bad else "OK:", bad or f"{len(BLOCK)} blocked, {len(PASS)} allowed")
sys.exit(1 if bad else 0)
