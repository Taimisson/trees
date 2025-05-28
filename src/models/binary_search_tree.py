from .binary_tree import BinaryTree
from .node import Node

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return None
        if node.data == value:
            return BinaryTree(node=node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def min(self, node=None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node
    
    def max(self, node=None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right
        return node
    
    def remove(self, value, node=None):
        if node is None:
            node = self.root
        
        if node is None:
            return None

        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute.data
                node.right = self.remove(substitute.data, node.right)
        return node 