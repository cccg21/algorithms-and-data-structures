import heapq
import sys

class Point:
     def __init__(self, t, l):
            self.t = t
            self.l = l

     def sum(self):
            return self.t + self.l

data = sys.stdin.read().split()
n = int(data[0])
pos = 1
arr = []

for _ in range(n):
    t = int(data[pos])
    l = int(data[pos+1])
    arr.append(Point(t, l))
    pos += 2

arr.sort(key=lambda c: c.t)

heap = []
total = 0

for i in range(n):
    while heap and heap[0] <= arr[i].t:
        heapq.heappop(heap)
    heapq.heappush(heap, arr[i].sum())
    if total < len(heap):
        total = len(heap)

print(total)