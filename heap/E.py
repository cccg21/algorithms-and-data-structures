import heapq
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heap = []
    pos = 1

    for _ in range(n):
        num = int(data[pos])
        heapq.heappush(heap, num)
        pos += 1

    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        s = a + b
        heapq.heappush(heap, s)
        total += s

    print(f"{total * 0.05:.2f}")

main()