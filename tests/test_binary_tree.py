import unittest
from src.models.binary_tree import BinaryTree
from src.models.node import Node

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def test_create_empty_tree(self):
        self.assertIsNone(self.tree.root)

    def test_create_tree_with_root(self):
        tree = BinaryTree(10)
        self.assertEqual(tree.root.data, 10)

    def test_create_tree_with_node(self):
        node = Node(10)
        tree = BinaryTree(node=node)
        self.assertEqual(tree.root.data, 10)

    def test_height_empty_tree(self):
        self.assertEqual(self.tree.height(), 0)

    def test_height_single_node(self):
        self.tree = BinaryTree(10)
        self.assertEqual(self.tree.height(), 1)

    def test_height_multiple_nodes(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.left = Node(2)
        self.tree = BinaryTree(node=root)
        self.assertEqual(self.tree.height(), 3)

if __name__ == '__main__':
    unittest.main() 