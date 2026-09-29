import sys

def nearby_binary_search(arr1, arr2):
    for x in arr2:
        low, high = 0, len(arr1)-1
        while low <= high:
            mid = (low + high) // 2
            if arr1[mid] == x:
                low = mid
                break
            if arr1[mid] > x:
                high = mid - 1
            else:
                low = mid + 1

        if low < len(arr1) and arr1[low] == x:
            print(f"{arr1[low]}")
        else:
            left = arr1[low - 1] if low - 1 >= 0 else None
            right = arr1[low] if low < len(arr1) else None

            if left is None:
                print(right)
            elif right is None:
                print(left)
            else:
                x_left = x - left
                x_right = right - x
                if x_left <= x_right:
                    print(left)
                else:
                    print(right)


n, k = map(int, input().split())
if n <= 0 or k > 10**5 + 1:
    sys.exit('Out of range')

arr1 = list(map(int, input().split()))
if len(arr1) > n:
    sys.exit()

arr2 = list(map(int, input().split()))
if len(arr2) > k:
    sys.exit()

nearby_binary_search(arr1, arr2)