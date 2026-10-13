from collections import deque

n, k = map(int, input().split())

posled = list(map(int, input().split()))
d = deque()

for i in range(n):
    x = posled[i]

    while d and posled[d[-1]] > x:
        d.pop()
    d.append(i)

    if d[0] <= i - k:
        d.popleft()
    if i >= k-1:
        print(posled[d[0]])