import sys

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
pos = 2

g = [[] for _ in range(n)]
while pos < len(data):
    v = int(data[pos]) - 1
    u = int(data[pos+1]) - 1
    g[u].append(v)
    g[v].append(u)
    pos += 2

visited = [False] * n
stack = [0]
visited[stack[0]] = True

while stack:
    v = stack.pop()

    for u in g[v]:
        if not visited[u]:
            stack.append(u)
            visited[u] = True

if m != n - 1:
    print("NO")
    sys.exit()
else:
    for i in range(n):
        if not visited[i]:
            print("NO")
            sys.exit()

print("YES")