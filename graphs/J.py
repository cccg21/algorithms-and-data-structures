import sys

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
pos = 2

g = [[] for _ in range(n)]
for _ in range(m):
    u = int(data[pos]) - 1
    v = int(data[pos + 1]) - 1
    pos += 2
    g[u].append(v)

order = list(map(int, data[pos:pos + n]))

position = [0] * n

for i in range(n):
    position[order[i] - 1] = i

for u in range(n):
    for v in g[u]:
        if position[u] >= position[v]:
            print("NO")
            sys.exit()

print("YES")

