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

    def find_par(self, node):
        if node is None:
            return

        self.find_par(node.left)
        if node.left and node.right:
            print(node.value)
        self.find_par(node.right)

data = sys.stdin.read().split()
tree = Tree()

for x in data:
    value = int(x)
    if value == 0:
        break
    tree.add(value)

tree.find_par(tree.root)


