tokens = input().split()
stack = []

for t in tokens:
    if t in '+-*':
        b = int(stack.pop())
        a = int(stack.pop())
        if t == '+':
            stack.append(a + b)
        elif t == '-':
            stack.append(a - b)
        else:
            stack.append(a * b)
    else:
        stack.append(int(t))

print(stack[0])
