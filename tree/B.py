import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.level = 0

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            self.level = 1
            return

        node = self.root
        depth = 1
        while True:
            if value == node.value:
                return
            depth += 1
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    break
                node = node.right

        self.level = max(self.level, depth)

data = sys.stdin.read().split()
tree = BinaryTree()

for x in data:
    value = int(x)
    if value == 0:
        break
    tree.add(value)

print(tree.level)