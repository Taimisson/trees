from .binary_search_tree import BinarySearchTree
from .node import Node

class AVLTree(BinarySearchTree):
    def calcHeight(self, node):
        if not node:
            return 0
        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.left) - self.calcHeight(node.right)

    def updateHeight(self, node):
        node.height = 1 + max(self.calcHeight(node.left), self.calcHeight(node.right))

    def rotateRight(self, node):
        print("Rotacionando para a direita", node.data)

        left_child = node.left
        temp = left_child.right

        left_child.right = node
        node.left = temp

        self.updateHeight(node)
        self.updateHeight(left_child)

        return left_child

    def rotateLeft(self, node):
        print("Rotacionando para a esquerda", node.data)

        right_child = node.right
        temp = right_child.left

        right_child.left = node
        node.right = temp

        self.updateHeight(node)
        self.updateHeight(right_child)

        return right_child

    def insert(self, value):
        self.root = self._insert(value, self.root)

    def _insert(self, value, node):
        if not node:
            return Node(value)

        if value < node.data:
            node.left = self._insert(value, node.left)
        else:
            node.right = self._insert(value, node.right)

        self.updateHeight(node)
        return self.settleViolation(value, node)

    def settleViolation(self, value, node):
        balance = self.calcBalance(node)

        if balance > 1 and value < node.left.data:
            return self.rotateRight(node)

        if balance < -1 and value > node.right.data:
            return self.rotateLeft(node)

        if balance > 1 and value > node.left.data:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        if balance < -1 and value < node.right.data:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    def remove(self, value, node=None):
        if node is None:
            node = self.root
        return self._remove(value, node)

    def _remove(self, value, node):
        if not node:
            return node

        if value < node.data:
            node.left = self._remove(value, node.left)
        elif value > node.data:
            node.right = self._remove(value, node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.min(node.right)
            node.data = temp.data
            node.right = self._remove(temp.data, node.right)

        if not node:
            return node

        self.updateHeight(node)
        balance = self.calcBalance(node)

        if balance > 1 and self.calcBalance(node.left) >= 0:
            return self.rotateRight(node)

        if balance < -1 and self.calcBalance(node.right) <= 0:
            return self.rotateLeft(node)

        if balance > 1 and self.calcBalance(node.left) < 0:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        if balance < -1 and self.calcBalance(node.right) > 0:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node 