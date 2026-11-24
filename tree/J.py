import sys

class Node:
    def __init__(self, value, freq=1):
        self.value = value
        self.freq = freq
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
                node.freq += 1
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

    def print_freq(self, node):
        if node is None:
            return

        self.print_freq(node.left)
        print(str(node.value) + " " + str(node.freq))
        self.print_freq(node.right)

data = sys.stdin.read().split()
tree = Tree()

for value in data:
    x = int(value)
    if x == 0:
        break
    tree.add(x)

tree.print_freq(tree.root)