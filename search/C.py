import sys
import math

def solve(C):
    low, high = 0, 10**12
    for _ in range(100):
        mid = (low + high) / 2
        if mid**2 + math.sqrt(mid) < C:
            low = mid
        else:
            high = mid
    return (low + high) / 2

x = float(input())
if x <= 1.0 or x >= 10**10:
    sys.exit('Out of range')

result = solve(x)
print(result)