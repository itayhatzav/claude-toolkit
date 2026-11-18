"""PreToolUse guard for Bash. Blocks: push to main/master, git add of everything, force push
(not --force-with-lease), git reset --hard, git clean --force (not a dry run), and rm -rf on the
root, the home folder, the current or parent folder or a bare star.

The command is split into real commands first (outside quotes), so text inside a quoted
string, such as a commit message that talks about these commands, is not blocked."""
import sys, json, re, shlex, os

DANGEROUS_RM = {"", "~", ".", "..", "*", "$HOME", "${HOME}", "$PWD", "${PWD}", "$(pwd)", "`pwd`",
                "/home", "/Users", "/root", "/etc", "/usr", "/var", "/bin", "/lib", "/opt", "/boot"}
WRAPPERS = {"sudo", "command", "exec", "nohup", "time", "env", "nice"}
SHELLS = {"bash", "sh", "zsh", "dash"}


def split_commands(cmd):
    """Split on ; & | newline and bare parentheses, but not inside quotes or $( ... )."""
    parts, cur, quote, i, n = [], [], None, 0, len(cmd)
    while i < n:
        ch = cmd[i]
        if quote:
            cur.append(ch)
            if ch == "\\" and quote == '"' and i + 1 < n:
                i += 1
                cur.append(cmd[i])
            elif ch == quote:
                quote = None
        elif ch == "\\" and i + 1 < n:
            cur.append(ch)
            i += 1
            cur.append(cmd[i])
        elif ch in "'\"`":
            quote = ch
            cur.append(ch)
        elif ch == "$" and cmd[i + 1:i + 2] == "(":
            depth, j = 0, i + 1
            while j < n:
                depth += (cmd[j] == "(") - (cmd[j] == ")")
                j += 1
                if depth == 0:
                    break
            cur.append(cmd[i:j])
            i = j - 1
        elif ch in ";&|\n()":
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
        i += 1
    parts.append("".join(cur))
    return [p for p in parts if p.strip()]


def tokens_of(segment):
    try:
        return shlex.split(segment)
    except ValueError:
        return segment.split()


def short_flags(tokens):
    return "".join(t[1:] for t in tokens if t.startswith("-") and not t.startswith("--"))


def rm_target_bad(t):
    t = t.strip("'\"")
    if t.endswith("/*"):
        t = t[:-2]
    t = t.rstrip("/")
    home = os.path.expanduser("~").rstrip("/")
    return t in DANGEROUS_RM or (home and t == home)


def check(tokens, depth=0):
    """Return a reason string if this one command is blocked, else None."""
    while tokens and (tokens[0] in WRAPPERS or re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", tokens[0])):
        tokens = tokens[1:]
    if not tokens:
        return None
    prog = os.path.basename(tokens[0])
    rest = tokens[1:]
    if prog in SHELLS and "-c" in rest and depth < 3:
        k = rest.index("-c")
        if k + 1 < len(rest):
            return check_string(rest[k + 1], depth + 1)
        return None
    if prog == "rm":
        end = rest.index("--") if "--" in rest else len(rest)
        flags, targets = rest[:end], rest[end + 1:] + [t for t in rest[:end] if not t.startswith("-")]
        sf = short_flags(flags)
        recursive = "r" in sf or "R" in sf or "--recursive" in flags
        force = "f" in sf or "--force" in flags
        if recursive and force and any(rm_target_bad(t) for t in targets):
            return "rm -rf on the root, home, current or parent folder, or a bare star"
        return None
    if prog != "git":
        return None
    i = 0
    while i < len(rest) and rest[i].startswith("-"):
        i += 2 if rest[i] in ("-C", "-c") else 1
    if i >= len(rest):
        return None
    sub, args = rest[i], rest[i + 1:]
    sf = short_flags(args)
    if sub == "add" and any(a in ("-A", "--all", ".") for a in args):
        return "git add of everything (stage files by name)"
    if sub == "push":
        refs = [a for a in args if not a.startswith("-")]
        if any(r in ("main", "master") or re.search(r"(:|/)(main|master)$", r) for r in refs):
            return "push to main (open a pull request)"
        if "--force" in args or (sf and "f" in sf):
            return "force push"
    if sub == "reset" and "--hard" in args:
        return "git reset --hard"
    if sub == "clean":
        force = "--force" in args or "f" in sf
        dry = "--dry-run" in args or "n" in sf
        if force and not dry:
            return "git clean --force"
    return None


def check_string(cmd, depth=0):
    for seg in split_commands(cmd):
        why = check(tokens_of(seg), depth)
        if why:
            return why
    return None


LEGACY = [
    r"git\s+push\b[^\n;&|]*\b(main|master)\b",
    r"git\s+add\s+(-A|--all|\.)(\s|$)",
    r"git\s+push\b[^\n;&|]*(--force\b|\s-f\b)(?!-with-lease)",
]


def main():
    d = json.load(sys.stdin)
    cmd = (d.get("tool_input") or {}).get("command") or ""
    try:
        why = check_string(cmd)
    except Exception:  # never let a parsing bug open the gate: fall back to the plain patterns
        why = "a blocked git command" if any(re.search(p, cmd) for p in LEGACY) else None
    if why:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Blocked by claude-toolkit: " + why + ". Use a branch and a PR, stage files by name, and ask Itay before anything destructive."}}))


main()
