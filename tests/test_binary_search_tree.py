import unittest
from src.models.binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def test_insert_single_value(self):
        self.tree.insert(10)
        self.assertEqual(self.tree.root.data, 10)

    def test_insert_multiple_values(self):
        values = [10, 5, 15, 3, 7, 12, 17]
        for value in values:
            self.tree.insert(value)
        
        self.assertEqual(self.tree.root.data, 10)
        self.assertEqual(self.tree.root.left.data, 5)
        self.assertEqual(self.tree.root.right.data, 15)
        self.assertEqual(self.tree.root.left.left.data, 3)
        self.assertEqual(self.tree.root.left.right.data, 7)
        self.assertEqual(self.tree.root.right.left.data, 12)
        self.assertEqual(self.tree.root.right.right.data, 17)

    def test_search_existing_value(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        
        result = self.tree.search(5)
        self.assertIsNotNone(result)
        self.assertEqual(result.root.data, 5)

    def test_search_nonexistent_value(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        
        result = self.tree.search(20)
        self.assertIsNone(result)

    def test_remove_leaf_node(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        
        self.tree.remove(5)
        self.assertIsNone(self.tree.root.left)

    def test_remove_node_with_one_child(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        
        self.tree.remove(5)
        self.assertEqual(self.tree.root.left.data, 3)

    def test_remove_node_with_two_children(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        
        self.tree.remove(5)
        self.assertEqual(self.tree.root.left.data, 7)
        self.assertEqual(self.tree.root.left.left.data, 3)

if __name__ == '__main__':
    unittest.main() 