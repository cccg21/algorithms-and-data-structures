import sys

def sift(heap, i, size):
    while i < size:
        l, r, m = 2*i + 1, 2*i + 2, i
        if l < size and heap[l] < heap[m]:
            m = l
        if r < size and heap[r] < heap[m]:
            m = r
        if m == i:
            break
        heap[i], heap[m] = heap[m], heap[i]
        i = m

def heapSort(heap):
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        sift(heap, i, n)
    for end in range(n - 1, 0, -1):
        heap[0], heap[end] = heap[end], heap[0]  # минимум уехал в конец
        sift(heap, 0, end)

n = int(input())
arr = list(map(int, sys.stdin.read().split()))

heapSort(arr)
arr.reverse()
print(*arr)