"""Checks hooks/guard.py: every dangerous command is blocked, every ordinary one passes.
Run: python3 -I hooks/test_guard.py"""
import json, os, subprocess, sys

GUARD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guard.py")
HOOKS_JSON = os.path.join(os.path.dirname(GUARD), "hooks.json")
BLOCK = [
    "git push origin main", "git push origin HEAD:main", "git add -A", "git add --all", "git add .",
    "git push -f origin x", "git push --force origin x", "git push -fu origin x",
    "git reset --hard HEAD~1", "git -C repo reset --hard", "cd x && git reset --hard",
    "git status; git reset --hard origin/x", "(cd x && git reset --hard)",
    "git clean -fd", "git clean -fdx", "git clean --force -d",
    "rm -rf /", "rm -rf ~", "rm -rf $HOME", "rm -rf \"$HOME\"", "rm -rf ${HOME}", "rm -rf $HOME/*",
    "rm -rf .", "rm -rf \".\"", "rm -rf ..", "rm -rf *", "rm -fr /", "rm -r -f ~/", "rm -f -r /",
    "rm -rf ./*", "rm -rf -- /", "rm --recursive --force /", "rm -r --force ~", "rm -rf \"$PWD\"",
    "rm -rf $(pwd)", "sudo rm -rf /", "rm -Rf /", "rm -rf /home", "bash -c 'rm -rf /'",
    "echo ok && rm -rf ~/",
]
PASS = [
    "git push --force-with-lease origin x", "git add CLAUDE.md", "git add kits/x/kit.json",
    "git reset --soft HEAD~1", "git reset HEAD file", "git reset --keep HEAD~1",
    "git clean -n", "git clean -nd", "git clean --dry-run", "git clean -n -e build-files",
    "git clean -n -- docs-final", "git clean -n --exclude=-foo",
    "rm -rf build/", "rm -rf ./build", "rm -rf ../tmp-copy", "rm -rf .git", "rm file.txt",
    "rm -r build", "rm -rf /tmp/x", "rm -rf *.pyc",
    "git push origin claude/x", "git push origin claude/main-fix", "git push -u origin itay/new-kit",
    "git commit -m \"guard now blocks git reset --hard and rm -rf /\"",
    "echo \"git push origin main\"", "grep 'git clean -f' notes.md",
    "git commit -m \"$(cat <<'EOF'\nnote about rm -rf / and git add -A\nEOF\n)\"",
    "ls -la", "python3 -I tools/kit.py check kits/x 2>&1 | tail -5",
]


def blocked(cmd):
    out = subprocess.run([sys.executable, "-I", GUARD], input=json.dumps({"tool_input": {"command": cmd}}),
                         capture_output=True, text=True).stdout.strip()
    return bool(out) and json.loads(out)["hookSpecificOutput"]["permissionDecision"] == "deny"


hooks = json.load(open(HOOKS_JSON))["hooks"]["PreToolUse"][0]
assert hooks["matcher"] == "Bash" and "guard.py" in hooks["hooks"][0]["command"], "hooks.json does not call guard.py"
bad = ["should block: " + c for c in BLOCK if not blocked(c)] + ["should pass: " + c for c in PASS if blocked(c)]
print("FAIL:" if bad else "OK:", bad or f"{len(BLOCK)} blocked, {len(PASS)} allowed")
sys.exit(1 if bad else 0)
