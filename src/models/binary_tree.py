from queue import Queue
from .node import Node

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end=" ")

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=" ")
        if node.right:
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        print(node, end=" ")
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)

    def height(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return 0
        
        left_height = 0
        right_height = 0
        
        if node.left:
            left_height = self.height(node.left)
        if node.right:
            right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)

    def level_order_traversal(self, node=None):
        if node is None:
            node = self.root
        
        queue = Queue()
        queue.put(node)

        while not queue.empty():
            current = queue.get()
            if current is None:
                continue
            print(current, end=" ")

            if current.left:
                queue.put(current.left)
            if current.right:
                queue.put(current.right)

        print()

    def build_tree_str(self, node=None, prefix="", is_left=True, lines=None):
        if lines is None:
            lines = []
        if node is None:
            node = self.root

        if node is None:
            return lines

        if node.right:
            new_prefix = prefix + ("│   " if is_left else "    ")
            self.build_tree_str(node.right, new_prefix, False, lines)

        connector = "└── " if is_left else "┌── "

        bf = 0
        if hasattr(self, 'calcBalance'):
            bf = self.calcBalance(node)

        lines.append(prefix + connector + f"{node.data} ({bf})")

        if node.left:
            new_prefix = prefix + ("    " if is_left else "│   ")
            self.build_tree_str(node.left, new_prefix, True, lines)

        return lines

    def print_tree(self):
        for line in self.build_tree_str():
            print(line) 