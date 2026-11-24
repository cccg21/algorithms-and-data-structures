import sys

data = sys.stdin.read().split()
n = int(data[0])
pos = 1
row = []

a = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(data[pos])
        pos += 1

flag = True
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i] or a[i][i] != 0:
            flag = False

if flag:
    print("YES")
else:
    print("NO")