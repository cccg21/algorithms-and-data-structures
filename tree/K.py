import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        node = self.root
        while node:
            if value == node.value:
                return
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    return
                node = node.right

    def find_pred(self, value):
        node = self.root
        minimum = -1
        while node:
            if node.value >= value:
                minimum = node.value
                node = node.left
            else:
                node = node.right
        return minimum

data = sys.stdin.read().split()

n = int(data[0])
pos = 1
tree = Tree()
last_n = 0

while pos < len(data):
    if data[pos] == '+':
        if data[pos-2] == '?':
            num = (int(data[pos+1]) + last_n) % 10**9
            tree.add(num)
            pos += 2
        else:
            tree.add(int(data[pos+1]))
            pos += 2
    elif data[pos] == '?':
        last_n = tree.find_pred(int(data[pos+1]))
        print(last_n)
        pos += 2