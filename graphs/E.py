import sys

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
pos = 2

g = [[] for _ in range(n)]
for _ in range(m):
    v = int(data[pos]) - 1
    u = int(data[pos+1]) - 1
    pos += 2
    g[v].append(u)
    g[u].append(v)

visited = [False] * n

def dfs(v):
    stack = [v]

    while stack:
        v = stack.pop()

        if visited[v]:
            continue

        visited[v] = True
        res.append(v + 1)

        for u in g[v]:
            if not visited[u]:
                stack.append(u)

components = []

for v in range(n):
    if not visited[v]:
        res = []
        dfs(v)
        components.append(res)

print(len(components))
for comp in components:
    print(len(comp))
    print(*comp)