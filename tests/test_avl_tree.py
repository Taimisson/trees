import unittest
from src.models.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_insert_single_value(self):
        self.tree.insert(10)
        self.assertEqual(self.tree.root.data, 10)
        self.assertEqual(self.tree.root.height, 1)

    def test_insert_with_right_rotation(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(2)
        
        self.assertEqual(self.tree.root.data, 5)
        self.assertEqual(self.tree.root.left.data, 2)
        self.assertEqual(self.tree.root.right.data, 10)

    def test_insert_with_left_rotation(self):
        self.tree.insert(10)
        self.tree.insert(15)
        self.tree.insert(20)
        
        self.assertEqual(self.tree.root.data, 15)
        self.assertEqual(self.tree.root.left.data, 10)
        self.assertEqual(self.tree.root.right.data, 20)

    def test_insert_with_left_right_rotation(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(7)
        
        self.assertEqual(self.tree.root.data, 7)
        self.assertEqual(self.tree.root.left.data, 5)
        self.assertEqual(self.tree.root.right.data, 10)

    def test_insert_with_right_left_rotation(self):
        self.tree.insert(10)
        self.tree.insert(15)
        self.tree.insert(12)
        
        self.assertEqual(self.tree.root.data, 12)
        self.assertEqual(self.tree.root.left.data, 10)
        self.assertEqual(self.tree.root.right.data, 15)

    def test_remove_leaf_node(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        
        self.tree.remove(5)
        self.assertIsNone(self.tree.root.left)
        self.assertEqual(self.tree.root.data, 10)
        self.assertEqual(self.tree.root.right.data, 15)

    def test_remove_node_with_one_child(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        
        self.tree.remove(5)
        self.assertEqual(self.tree.root.left.data, 3)
        self.assertEqual(self.tree.root.data, 10)
        self.assertEqual(self.tree.root.right.data, 15)

    def test_remove_node_with_two_children(self):
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        
        self.tree.remove(5)
        self.assertEqual(self.tree.root.left.data, 7)
        self.assertEqual(self.tree.root.left.left.data, 3)
        self.assertEqual(self.tree.root.data, 10)
        self.assertEqual(self.tree.root.right.data, 15)

if __name__ == '__main__':
    unittest.main() 