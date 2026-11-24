import sys

data = sys.stdin.read().split()
n = int(data[0])
pos = 1

g = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        g[i][j] = int(data[pos])
        pos += 1

def dfs(v, visited):
    stack = [v]

    while stack:
        v = stack.pop()

        for u in range(n):
            if g[v][u] == 1 and not visited[u]:
                stack.append(u)
                visited[u] = True

for v in range(n):
    visited = [False] * n
    dfs(v, visited)
    if visited[v]:
        print("1")
        sys.exit()

print("0")