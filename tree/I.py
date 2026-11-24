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

    def balanced_tree(self, node):
        if node is None:
            return False
        left = self.balanced_tree(node.left)
        if left == -1:
            return -1
        right = self.balanced_tree(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

data = sys.stdin.read().split()
tree = Tree()

for value in data:
    x = int(value)
    if x == 0:
        break
    tree.add(x)

if tree.balanced_tree(tree.root) == -1:
    print('NO')
else:
    print('YES')