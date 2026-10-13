n = int(input())
vagoni = list(map(int, input().split()))
need = 1
stack = []

for i in range(n):
    stack.append(vagoni[i])

    while stack and stack[-1] == need:
        stack.pop()
        need += 1

if not stack:
    print("YES")
else:
    print("NO")