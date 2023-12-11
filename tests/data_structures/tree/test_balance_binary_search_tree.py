import unittest
from src.data_structures.tree.balance_binary_search_tree import balance_tree, is_balanced
from src.data_structures.tree.binary_search_tree import BinarySearchTree

class TestBalanceTree(unittest.TestCase):

    def setUp(self):
        self.bst1 = BinarySearchTree()
        self.bst2 = BinarySearchTree()
        self.bst3 = BinarySearchTree()

        # Case 1
        self.bst1.insert(30)
        self.bst1.insert(20)
        self.bst1.insert(10)

        # Case 2
        self.bst2.insert(4)
        self.bst2.insert(3)
        self.bst2.insert(2)
        self.bst2.insert(1)

        # Case 3
        self.bst3.insert(4)
        self.bst3.insert(3)
        self.bst3.insert(2)
        self.bst3.insert(1)
        self.bst3.insert(5)
        self.bst3.insert(6)
        self.bst3.insert(7)

    def test_balance_tree_case1(self):
        balanced_bst = balance_tree(self.bst1.root)
        self.assertTrue(is_balanced(balanced_bst))

    def test_balance_tree_case2(self):
        balanced_bst = balance_tree(self.bst2.root)
        self.assertTrue(is_balanced(balanced_bst))

    def test_balance_tree_case3(self):
        balanced_bst = balance_tree(self.bst3.root)
        self.assertTrue(is_balanced(balanced_bst))

if __name__ == '__main__':
    unittest.main()
