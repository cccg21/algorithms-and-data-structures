queue = []

while True:
    line = input().split()

    if not line:
        continue

    cmd = line[0]

    if cmd == 'push' and len(line) == 2:
        queue.append(int(line[1]))
        print("ok")

    elif cmd == 'pop':
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print("error")

    elif cmd == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print("error")

    elif cmd == 'size':
        print(len(queue))

    elif cmd == 'clear':
        while len(queue) > 0:
            queue.pop(0)
        if len(queue) == 0:
            print("ok")

    elif cmd == 'exit':
        print("bye")
        break