import sys

n, k = map(int, input().split())
if n <= 0 or k > 10**9:
    sys.exit()

arr1 = list(map(int, input().split()))
if len(arr1) > n:
    sys.exit()

for i in range(len(arr1)):
    if arr1[i] > 10**9:
        sys.exit()

arr2 = list(map(int, input().split()))
if len(arr2) > k:
    sys.exit()

for i in range(len(arr2)):
    if arr2[i] > 10**9:
        sys.exit()

def binary_search(arr1, arr2):
    for i in range(len(arr2)):
        low = 0
        high = len(arr1)-1
        while low <= high:
            mid = (low+high)//2
            if arr1[mid] < arr2[i]:
                low = mid + 1
            else:
                high = mid - 1

        if low < len(arr1) and arr1[low] == arr2[i]:
            print("YES")
        else:
            print("NO")


binary_search(arr1, arr2)