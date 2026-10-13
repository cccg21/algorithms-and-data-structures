from collections import deque
import sys

data = sys.stdin.read().split()
n = int(data[0])
pos = 1

first = deque()
second = deque()
res = []

for _ in range(n):
    cmd = data[pos]
    pos += 1
    if cmd == "+":
        second.append(int(data[pos]))
        pos += 1
        if len(second) > len(first):
            first.append(second.popleft())

    elif cmd == "*":
        second.appendleft(int(data[pos]))
        pos += 1
        if len(second) > len(first):
            first.append(second.popleft())

    elif cmd == "-":
        if len(first) != 0:
            res.append(first.popleft())
        if len(first) < len(second):
            first.append(second.popleft())

print('\n'.join(map(str,res)))