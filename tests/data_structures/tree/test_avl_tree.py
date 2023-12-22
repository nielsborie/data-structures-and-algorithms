import unittest

from src.data_structures.tree.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.myTree = AVLTree()
        self.root = None

    def test_subtree_balance_after_insertion(self):
        # Given an empty AVL tree
        values = [10, 20, 30, 40, 50, 25]

        # When inserting values into the AVL tree
        for val in values:
            self.root = self.myTree.insert(self.root, val)
            self.assertTrue(self.is_subtree_balanced(self.root))

        # Then all subtrees in the AVL tree should be balanced
        self.assertTrue(self.is_subtree_balanced(self.root))

    def test_subtree_balance_after_deletion(self):
        # Given an empty AVL tree
        values = [10, 20, 30, 40, 50, 25]

        # When inserting values into the AVL tree
        for val in values:
            self.root = self.myTree.insert(self.root, val)
            self.assertTrue(self.is_subtree_balanced(self.root))
        
        for val in reversed(values):
            self.root = self.myTree.delete(self.root, val)
            self.assertTrue(self.is_subtree_balanced(self.root))
        

    def is_subtree_balanced(self, root):
        # Helper function to check if a subtree is balanced

        # Base case: an empty subtree is balanced
        if root is None:
            return True

        # Check balance factor of the current node
        balance_factor = self.myTree.get_balance(root)
        if abs(balance_factor) > 1:
            return False

        # Recursively check balance of left and right subtrees
        left_balanced = self.is_subtree_balanced(root.left)
        right_balanced = self.is_subtree_balanced(root.right)

        # The subtree is balanced if both left and right subtrees are balanced
        return left_balanced and right_balanced

if __name__ == '__main__':
    unittest.main()
