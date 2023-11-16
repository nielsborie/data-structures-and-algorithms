import unittest
from io import StringIO
import sys

from src.data_structures.tree.binary_search_tree import Node

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
        self.tree = Node(5)
        self.tree.insert(3)
        self.tree.insert(8)
        self.tree.insert(1)
        self.tree.insert(4)

    def test_insert(self):
        # Given
        value_to_insert = 2

        # When
        self.tree.insert(value_to_insert)

        # Then
        self.assertTrue(self.tree.contains(value_to_insert))

    def test_contains(self):
        # Given
        existing_value = 5
        non_existing_value = 2

        # When / Then
        self.assertTrue(self.tree.contains(existing_value))
        self.assertFalse(self.tree.contains(non_existing_value))

    def test_print_in_order(self):
        # Given
        expected_output = "1\n3\n4\n5\n8\n"

        # When
        with captured_output() as out:
            self.tree.print_in_order()

        # Then
        self.assertEqual(out.getvalue(), expected_output)

    def test_print_pre_order(self):
        # Given
        expected_output = "5\n3\n1\n4\n8\n"

        # When
        with captured_output() as out:
            self.tree.print_pre_order()

        # Then
        self.assertEqual(out.getvalue(), expected_output)

    def test_print_post_order(self):
        # Given
        expected_output = "1\n4\n3\n8\n5\n"

        # When
        with captured_output() as out:
            self.tree.print_post_order()

        # Then
        self.assertEqual(out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
