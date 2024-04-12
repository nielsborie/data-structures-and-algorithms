import unittest

from src.data_structures.linked_list.doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_insert_at_end(self):
        # Given
        self.dll.insert_at_end(1)

        # When
        self.dll.insert_at_end(2)

        # Then
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.head.next.prev.data, 1)

    def test_insert_at_beginning(self):
        # Given
        self.dll.insert_at_beginning(1)

        # When
        self.dll.insert_at_beginning(2)

        # Then
        self.assertEqual(self.dll.head.data, 2)
        self.assertEqual(self.dll.head.next.data, 1)
        self.assertEqual(self.dll.head.next.prev.data, 2)

    def test_insert_at_position(self):
        # Given
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(3)

        # When
        self.dll.insert_at_position(1, 2)

        # Then
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next.data, 2)
        self.assertEqual(self.dll.head.next.next.data, 3)
        self.assertEqual(self.dll.head.next.prev.data, 1)
        self.assertEqual(self.dll.head.next.next.prev.data, 2)

    def test_delete_at_end(self):
        # Given
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)

        # When
        self.dll.delete_at_end()

        # Then
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next, None)

    def test_delete_at_beginning(self):
        # Given
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)

        # When
        self.dll.delete_at_beginning()

        # Then
        self.assertEqual(self.dll.head.data, 2)
        self.assertEqual(self.dll.head.prev, None)

    def test_delete_at_position(self):
        # Given
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)

        # When
        self.dll.delete_at_position(1)

        # Then
        self.assertEqual(self.dll.head.data, 1)
        self.assertEqual(self.dll.head.next.data, 3)
        self.assertEqual(self.dll.head.next.prev.data, 1)

    def test_display_forward(self):
        # Given
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)

        # When
        result = self.dll.display_forward()

        # Then
        self.assertEqual(result, [1, 2, 3])

    def test_display_backward(self):
        # Given
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)

        # When
        result = self.dll.display_backward()

        # Then
        self.assertEqual(result, [3, 2, 1])

if __name__ == '__main__':
    unittest.main()