import unittest
from io import StringIO
import sys
from src.data_structures.tree.binary_search_tree import BinarySearchTree, TreeNode, delete_node

class captured_output:
    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.new_stdout = StringIO()
        return self.new_stdout

    def __exit__(self, *args):
        sys.stdout = self.old_stdout

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        # Given
        # Create a simple tree for testing
        #       5
        #      / \
        #     3   8
        #    / \
        #   1   4
        self.bst = BinarySearchTree()
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(8)
        self.bst.insert(1)
        self.bst.insert(4)

    def test_insert(self):
        # Given
        value_to_insert = 2

        # When
        self.bst.insert(value_to_insert)

        # Then
        self.assertTrue(self.bst.contains(value_to_insert))

    def test_contains(self):
        # Given
        existing_value = 5
        non_existing_value = 2

        # When / Then
        self.assertTrue(self.bst.contains(existing_value))
        self.assertFalse(self.bst.contains(non_existing_value))

    def test_print_in_order(self):
        # Given
        expected_output = "1\n3\n4\n5\n8\n"

        # When
        with captured_output() as out:
            self.bst.print_in_order()

        # Then
        self.assertEqual(out.getvalue(), expected_output)

    def test_print_pre_order(self):
        # Given
        expected_output = "5\n3\n1\n4\n8\n"

        # When
        with captured_output() as out:
            self.bst.print_pre_order()

        # Then
        self.assertEqual(out.getvalue(), expected_output)

    def test_print_post_order(self):
        # Given
        expected_output = "1\n4\n3\n8\n5\n"

        # When
        with captured_output() as out:
            self.bst.print_post_order()

        # Then
        self.assertEqual(out.getvalue(), expected_output)

    def test_get_height_depth_first_search(self):
        # Given
        expected_height = 3

        # When
        result = self.bst.get_height_depth_first_search()

        # Then
        self.assertEqual(result, expected_height)

    def test_get_height_breadth_first_search(self):
        # Given
        expected_height = 3

        # When
        result = self.bst.get_height_breadth_first_search()

        # Then
        self.assertEqual(result, expected_height)
    
    def test_get_height_recursive(self):
        # Given
        expected_height = 3

        # When
        result = self.bst.get_height_recursive()

        # Then
        self.assertEqual(result, expected_height)

class TestTreeNodeDeleteNode(unittest.TestCase):
    def setUp(self):
        # Create a sample BST
        keys = [30, 70, 20, 40, 60, 80]
        self.root = TreeNode(value=50)
        for key in keys:
            self.root.insert(key)

    def test_delete_leaf_node(self):
        # Delete a leaf node (no children)
        self.root.delete_node(20)
        self.assertIsNone(self.root.left.left)

    def test_delete_node_with_one_child(self):
        # Delete a node with one child
        self.root = self.root.delete_node(30)
        self.assertEqual(self.root.left.data, 40)

    def test_delete_node_with_two_children(self):
        # Delete a node with two children
        self.root = self.root.delete_node(30)
        self.assertEqual(self.root.left.data, 40)

    def test_delete_root_node(self):
        # Delete the root node
        self.root = self.root.delete_node(50)
        self.assertEqual(self.root.data, 60)

    def test_delete_nonexistent_node(self):
        # Attempt to delete a node that doesn't exist
        self.root = self.root.delete_node(90)
        self.assertIsNotNone(self.root)
        self.assertEqual(self.root.data, 50)

    def test_delete_last_node(self):
        # Delete the last remaining node
        # Delete the last remaining node
        self.root = self.root.delete_node(50)
        self.root = self.root.delete_node(30)
        self.root = self.root.delete_node(40)
        self.root = self.root.delete_node(60)
        self.root = self.root.delete_node(70)
        self.root = self.root.delete_node(20)
        self.root = self.root.delete_node(80)
        self.assertIsNone(self.root)

    def test_delete_node_unbalanced_tree(self):
        # Create an unbalanced tree
        unbalanced_tree = TreeNode(50)
        unbalanced_tree.right = TreeNode(60)
        unbalanced_tree.right.right = TreeNode(70)
        unbalanced_tree.right.right.right = TreeNode(80)
        unbalanced_tree.left = TreeNode(40)  # Ajouter un nœud gauche pour corriger l'erreur

        # Delete a node in the unbalanced tree
        unbalanced_tree = unbalanced_tree.delete_node(60)
        self.assertEqual(unbalanced_tree.data, 50)
        self.assertEqual(unbalanced_tree.right.right.data, 80)


class TestDeleteNodeFunction(unittest.TestCase):
    def setUp(self):
        # Helper function to create a BST
        def insert_keys(root, keys):
            for key in keys:
                root = insert_key(root, key)
            return root

        # Helper function to insert a key into a BST
        def insert_key(root, key):
            if root is None:
                return TreeNode(key)
            if key < root.data:
                root.left = insert_key(root.left, key)
            elif key > root.data:
                root.right = insert_key(root.right, key)
            return root

        # Create a sample BST
        keys = [50, 30, 70, 20, 40, 60, 80]
        self.root = None
        for key in keys:
            self.root = insert_key(self.root, key)

    def test_delete_leaf_node(self):
        # Delete a leaf node (no children)
        self.root = delete_node(self.root, 20)
        self.assertIsNone(self.root.left.left)

    def test_delete_node_with_one_child(self):
        # Delete a node with one child
        self.root = delete_node(self.root, 30)
        self.assertEqual(self.root.left.data, 40)

    def test_delete_node_with_two_children(self):
        # Delete a node with two children
        self.root = delete_node(self.root, 30)
        self.assertEqual(self.root.left.data, 40)

    def test_delete_root_node(self):
        # Delete the root node
        self.root = delete_node(self.root, 50)
        self.assertEqual(self.root.data, 60)

    def test_delete_nonexistent_node(self):
        # Attempt to delete a node that doesn't exist
        self.root = delete_node(self.root, 90)
        self.assertIsNotNone(self.root)
        self.assertEqual(self.root.data, 50)

    def test_delete_last_node(self):
        # Delete the last remaining node
        self.root = delete_node(self.root, 50)
        self.root = delete_node(self.root, 30)
        self.root = delete_node(self.root, 40)
        self.root = delete_node(self.root, 60)
        self.root = delete_node(self.root, 70)
        self.root = delete_node(self.root, 20)
        self.root = delete_node(self.root, 80)
        self.assertIsNone(self.root)

    def test_delete_node_unbalanced_tree(self):
        # Create an unbalanced tree
        unbalanced_tree = TreeNode(50)
        unbalanced_tree.right = TreeNode(60)
        unbalanced_tree.right.right = TreeNode(70)
        unbalanced_tree.right.right.right = TreeNode(80)

        # Delete a node in the unbalanced tree
        unbalanced_tree = delete_node(unbalanced_tree, 60)
        self.assertEqual(unbalanced_tree.data, 50)
        self.assertEqual(unbalanced_tree.right.right.data, 80)
        
if __name__ == '__main__':
    unittest.main()