import sys

data = sys.stdin.read().split()
n, s = int(data[0]), int(data[1])
pos = 2

g = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        g[i][j] = int(data[pos])
        pos += 1

visited = [False] * n
stack = [s-1]
visited[s-1] = True
count = 0

while stack:
    v = stack.pop()
    count += 1
    for u in range(n):
        if g[v][u] == 1 and not visited[u]:
            visited[u] = True
            stack.append(u)

print(count)