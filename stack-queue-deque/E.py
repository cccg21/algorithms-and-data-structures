deque = []

while True:
    line = input().split()

    if len(deque) > 100:
        break

    if not line:
        continue

    cmd = line[0]

    if cmd == 'push_front' and len(line) == 2:
        deque.insert(0, int(line[1]))
        print("ok")

    elif cmd == 'push_back' and len(line) == 2:
        deque.append(int(line[1]))
        print("ok")

    elif cmd == 'pop_front':
        if len(deque) > 0:
            print(deque.pop(0))
        else:
            print("error")

    elif cmd == 'pop_back':
        if len(deque) > 0:
            print(deque.pop())
        else:
            print("error")

    elif cmd == 'front':
        if len(deque) > 0:
            print(deque[0])
        else:
            print("error")

    elif cmd == 'back':
        if len(deque) > 0:
            print(deque[-1])
        else:
            print("error")

    elif cmd == 'size':
        print(len(deque))

    elif cmd == 'clear':
        while len(deque) > 0:
            deque.pop()
        if len(deque) == 0:
            print("ok")

    elif cmd == 'exit':
        print("bye")
        break