import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)

        node = self.root
        while node:
            if value == node.value:
                return
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                    break
                node = node.left
            if value > node.value:
                if node.right is None:
                    node.right = TreeNode(value)
                    break
                node = node.right

    def walk(self, node):
        if node is None:
            return

        self.walk(node.left)
        print(node.value, sep = "\n")
        self.walk(node.right)

data = sys.stdin.read().split()
tree = Tree()

for token in data:
    x = int(token)
    if x == 0:
        break
    tree.add(x)

tree.walk(tree.root)