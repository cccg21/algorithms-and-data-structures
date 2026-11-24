import sys

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
pos = 2

graph = [set() for _ in range(n)]
for _ in range(m):
    u = int(data[pos]) - 1
    v = int(data[pos+1]) - 1
    pos += 2
    graph[u].add(v)
    graph[v].add(u)

is_poln = True
for i in range(len(graph)):
    if len(graph[i]) != n-1:
        is_poln = False

if is_poln:
    print("YES")
else:
    print("NO")