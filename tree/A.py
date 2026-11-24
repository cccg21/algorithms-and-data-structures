import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def find(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            node = self.root
            while True:
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

    def delete(self, value):
        self.root = self._delete(self.root, value)
        return True

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            pred = node.left
            while pred.right:
                pred = pred.right
            node.value = pred.value
            node.left = self._delete(node.left, pred.value)

        return node

    def print_tree(self):
        self._print(self.root, 0)

    def _print(self, node, level):
        if node is None:
            return
        self._print(node.left, level + 1)
        print("." * level + str(node.value))
        self._print(node.right, level + 1)

def main():
    data = sys.stdin.read().split()
    tree = BinaryTree()
    pos = 0

    while pos < len(data):
        cmd = data[pos]

        if cmd == 'ADD':
            n = data[pos+1]
            if tree.find(int(n)):
                print("ALREADY")
            else:
                tree.insert(int(n))
                print("DONE")
            pos += 2

        elif cmd == 'DELETE':
            n = data[pos+1]
            if tree.find(int(n)):
                tree.delete(int(n))
                print("DONE")
            else:
                print("CANNOT")
            pos += 2

        elif cmd == 'SEARCH':
            n = data[pos+1]
            if tree.find(int(n)):
                print("YES")
            else:
                print("NO")
            pos += 2

        elif cmd == 'PRINTTREE':
            tree.print_tree()
            pos += 1

main()