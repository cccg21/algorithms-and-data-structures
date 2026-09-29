import sys

def solve_f(a,b,c,d):
    eps = 1e-12

    def f(x):
        return a*x**3 + b*x**2 + c*x + d

    if a > 0:
        low, high = -10000, 10000
        while high - low > eps:
            mid = (low + high) / 2
            if f(mid) == 0:
                break
            elif f(mid) > 0:
                high = mid
            else:
                low = mid
    else:
        low, high = 10000, -10000
        while low - high > eps:
            mid = (low + high) / 2
            if f(mid) == 0:
                break
            elif f(mid) > 0:
                high = mid
            else:
                low = mid
    return (low + high) / 2

a,b,c,d = map(int, input().split())
if a < -1000 or a > 1000 or b < -1000 or b > 1000\
        or c < -1000 or c > 1000 or d < -1000 or d > 1000:
    sys.exit('Out of range')

result = solve_f(a,b,c,d)
print(result)