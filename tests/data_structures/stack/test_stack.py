import unittest

from src.data_structures.stack.stack import Stack

class TestStack(unittest.TestCase):

    def test_empty_stack(self):
        stack = Stack()
        self.assertTrue(stack.empty())
        self.assertEqual(stack.size(), 0)
        with self.assertRaises(Exception):
            stack.pop()  # Trying to pop from an empty stack should raise an exception

    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.empty())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek().value, 1)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.empty())
        self.assertEqual(stack.size(), 0)
        with self.assertRaises(Exception):
            stack.pop()  # Trying to pop from an empty stack should raise an exception

    def test_multiple_push_pop(self):
        stack = Stack()
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            stack.push(element)

        self.assertFalse(stack.empty())
        self.assertEqual(stack.size(), len(elements))
        self.assertEqual(stack.peek().value, elements[-1])

        for element in reversed(elements):
            self.assertEqual(stack.pop(), element)

        self.assertTrue(stack.empty())
        self.assertEqual(stack.size(), 0)
        with self.assertRaises(Exception):
            stack.pop()  # Trying to pop from an empty stack should raise an exception

    def test_push_peek(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek().value, 1)
        stack.push(2)
        self.assertEqual(stack.peek().value, 2)

    def test_push_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)

    def test_push_pop_size(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)
        stack.pop()
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertEqual(stack.size(), 0)

if __name__ == '__main__':
    unittest.main()
