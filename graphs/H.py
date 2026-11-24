import sys

data = sys.stdin.read().split()
n = int(data[0])
pos = 1

g = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        g[i][j] = int(data[pos])
        pos += 1

start = int(data[pos]) - 1
end = int(data[pos+1]) - 1
out = []

dist = [-1] * n
dist[start] = 0
queue = [start]
head = 0

while head < len(queue):
    v = queue[head]
    head += 1
    out.append(v+1)

    for u in range(n):
        if g[v][u] == 1 and dist[u] == -1:
            dist[u] = dist[v] + 1
            queue.append(u)

if dist[end] == -1:
    print("-1")
else:
    print(dist[end])
    if dist[end] > 0:
        path = [end + 1]
        v = end
        while v != start:
            for u in range(n):
                if g[v][u] == 1 and dist[u] == dist[v] - 1:
                    v = u
                    break
            path.append(v+1)
        path.reverse()
        print(*path)