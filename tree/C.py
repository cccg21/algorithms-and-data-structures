import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            self.size = 1
            return

        node = self.root
        while node:
            if value == node.value:
                return
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    self.size += 1
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    self.size += 1
                    break
                node = node.right

data = sys.stdin.read().split()
tree = Tree()

for token in data:
    x = int(token)
    if x == 0:
        break
    tree.add(x)

print(tree.size)