import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heap = []
    out = []
    pos = 1

    for _ in range(n):
        cmd = data[pos]
        pos += 1
        if cmd == '0':
            x = int(data[pos])
            pos += 1
            heap.append(x)
            i = len(heap) - 1
            while i > 0:
                p = (i - 1) // 2
                if heap[i] <= heap[p]:
                    break
                heap[i], heap[p] = heap[p], heap[i]
                i = p
        else:
            top = heap[0]
            last = heap.pop()
            if heap:
                heap[0] = last
                i = 0
                size = len(heap)
                while True:
                    l, r, m = 2*i + 1, 2*i + 2, i
                    if l < size and heap[l] > heap[m]:
                        m = l
                    if r < size and heap[r] > heap[m]:
                        m = r
                    if m == i:
                        break
                    heap[i], heap[m] = heap[m], heap[i]
                    i = m
            out.append(top)

    print("\n".join(map(str, out)))

main()