import sys
import heapq

def main():
    data = sys.stdin.read().split()
    heap = []
    out = []
    pos = 0

    while pos < len(data):
        cmd = data[pos]
        pos += 1
        if cmd == 'ADD':
            n = int(data[pos])
            heapq.heappush(heap, -n)
            pos += 1
        elif cmd == 'EXTRACT':
            if heap:
                maxi = -heapq.heappop(heap)
                out.append(str(maxi))
            else:
                out.append('CANNOT')
        elif cmd == 'CLEAR':
            heap.clear()

    print('\n'.join(out))

main()