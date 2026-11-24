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
            return value

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

    def find_2_max(self):
        node = self.root
        sec_max = None

        while node.right:
            sec_max = node
            node = node.right

        if node.left:
            node = node.left
            while node.right:
                node = node.right
            return node.value

        return sec_max.value

data = sys.stdin.read().split()
tree = Tree()

for token in data:
    x = int(token)
    if x == 0:
        break
    tree.add(x)

print(tree.find_2_max())