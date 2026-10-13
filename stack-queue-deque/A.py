stack = []

while True:
    try:
        line = input().split()
    except EOFError:
        break

    if not line:
        continue

    cmd = line[0]

    if cmd == "push" and len(line) == 2:
        stack.append(int(line[1]))
        print("ok")

    elif cmd == "pop":
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()
        else:
            print("error")

    elif cmd == "back":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print("error")

    elif cmd == "size":
        print(len(stack))

    elif cmd == "clear":
        while len(stack) > 0:
            stack.pop()
        if len(stack) == 0:
            print("ok")

    elif cmd == "exit":
        print("bye")
        break
