import sys

data = sys.stdin.read().split()
n = int(data[0])
pos = 1
x1, y1, x2, y2 = [int(data[i])-1 for i in range(pos, len(data))]

moves = [(1, 2), (2, 1), (-1, 2), (-2, 1),
         (1, -2), (2, -1), (-1, -2), (-2, -1)]

dist = [[-1] * n for _ in range(n)]
parent = [[None] * n for _ in range(n)]

dist[x1][y1] = 0
queue = [(x1, y1)]
head = 0

while head < len(queue):
    x, y = queue[head]
    head += 1
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            parent[nx][ny] = (x, y)
            queue.append((nx, ny))

print(dist[x2][y2])

path = []
cur = (x2, y2)
while cur is not None:
    path.append(cur)
    cur = parent[cur[0]][cur[1]]
path.reverse()

for x, y in path:
    print(x + 1, y + 1)