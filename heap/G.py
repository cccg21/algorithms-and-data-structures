import heapq
import sys


def birth_time(size):
    return max(1000 - size, 1)

class Aquarium:
    def __init__(self, t, n, size):
        self.t = t
        self.n = n
        self.size = size

    def __lt__(self, other):
        return self.t < other.t

data = sys.stdin.read().split()
n = int(data[0])
pos = 1

heap = []
for i in range(n):
    num = i + 1  # номер аквариума
    size = int(data[pos])  # размер аквариума
    t = birth_time(size)  # время след. рождения
    heapq.heappush(heap, Aquarium(t, num, size))
    pos += 1

p = 1             #тек. позиция у аквариума
cur_time = 0      #тек. время

flag = True
while flag:
    n_a = heap[0].n
    t = heap[0].t
    if abs(n_a - p) > t - cur_time:
        print(heap[0].t)
        flag = False
    else:
        p = heap[0].n
        cur_time = heap[0].t

        aquarium = heapq.heappop(heap)
        aquarium.size += 1
        aquarium.t += birth_time(aquarium.size)
        heapq.heappush(heap, aquarium)