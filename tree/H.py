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

    def find_solo_high(self, node):
        if node is None:
            return

        self.find_solo_high(node.left)
        if node.left and node.right is None:
            print(node.value)
        elif node.right and node.left is None:
            print(node.value)
        self.find_solo_high(node.right)


data = sys.stdin.read().split()
tree = Tree()

for value in data:
    x = int(value)
    if x == 0:
        break
    tree.add(x)

tree.find_solo_high(tree.root)