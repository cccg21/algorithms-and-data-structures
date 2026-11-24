import sys

data = sys.stdin.read().split()
n = int(data[0])
pos = 1
sources = []
stocks = []

a = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(data[pos])
        pos += 1

for j in range(n):
    is_source = True
    for i in range(n):
        if a[i][j] == 1:
            is_source = False
    if is_source:
        sources.append(j+1)

for i in range(n):
    is_stock = True
    for j in range(n):
        if a[i][j] == 1:
            is_stock = False
    if is_stock:
        stocks.append(i+1)

print(len(sources))
for i in range(len(sources)):
    print(sources[i])

print(len(stocks))
for i in range(len(stocks)):
    print(stocks[i])