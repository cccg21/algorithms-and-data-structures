s = input().strip()

pairs = {')': '(', ']': '[', '}': '{'}
stack = []
ok = True

for ch in s:
    if ch in '([{':
        stack.append(ch)
    else:
        if not stack or stack.pop() != pairs[ch]:
            ok = False
            break

if stack:
    ok = False

print("yes" if ok else "no")