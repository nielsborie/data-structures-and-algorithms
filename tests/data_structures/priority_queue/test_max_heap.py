import unittest

from src.data_structures.priority_queue.max_heap import MaxHeap


class TestMinHeap(unittest.TestCase):

    def test_insert_and_peek(self):
        # Given
        max_heap = MaxHeap()

        # When
        max_heap.insert(4)
        max_heap.insert(2)
        max_heap.insert(8)

        # Then
        self.assertEqual(max_heap.peek(), 8)

    def test_poll(self):
        # Given
        max_heap = MaxHeap()
        max_heap.insert(4)
        max_heap.insert(2)
        max_heap.insert(8)

        # When
        extracted_value = max_heap.poll()

        # Then
        self.assertEqual(extracted_value, 8)
        self.assertEqual(max_heap.peek(), 4)

    def test_insert_and_poll_empty_heap(self):
        # Given
        max_heap = MaxHeap()

        # When
        with self.assertRaises(Exception) as context:
            max_heap.poll()

        # Then
        self.assertEqual(str(context.exception), "Cannot poll a value on an empty heap.")

    def test_peek_empty_heap(self):
        # Given
        max_heap = MaxHeap()

        # When
        with self.assertRaises(Exception) as context:
            max_heap.peek()

        # Then
        self.assertEqual(str(context.exception), "Cannot peek a value on an empty heap.")

    def test_insert_and_poll(self):
        # Given
        max_heap = MaxHeap()

        # When
        max_heap.insert(4)
        max_heap.insert(2)
        max_heap.insert(8)
        max_heap.insert(1)
        extracted_value = max_heap.poll()

        # Then
        self.assertEqual(extracted_value, 8)
        self.assertEqual(max_heap.peek(), 4)

    def test_multiple_inserts_and_polls(self):
        # Given
        max_heap = MaxHeap()

        # When
        max_heap.insert(4)
        max_heap.insert(2)
        max_heap.insert(8)
        max_heap.insert(1)
        max_heap.insert(5)
        extracted_values = [max_heap.poll() for _ in range(max_heap.size)]

        # Then
        expected_values = [8, 5, 4, 2, 1]
        self.assertEqual(extracted_values, expected_values)

    def test_update_by_index(self):
        # Given
        max_heap = MaxHeap()
        max_heap.insert(3)
        max_heap.insert(1)
        max_heap.insert(4)
        max_heap.insert(2)

        # When
        self.assertEqual(max_heap.heap, [4, 2, 3, 1])

        max_heap.update_by_index(2, 0)

        # Then
        self.assertEqual(max_heap.heap, [4, 2, 0, 1])

        # When
        max_heap.update_by_index(0, 5)

        # Then
        self.assertEqual(max_heap.heap, [5, 2, 0, 1])

        # When
        max_heap.update_by_index(3, 1)

        # Then
        self.assertEqual(max_heap.heap, [5, 2, 0, 1])

    def test_update(self):
        # Given
        max_heap = MaxHeap()
        max_heap.insert(3)
        max_heap.insert(1)
        max_heap.insert(4)
        max_heap.insert(2)

        # When
        max_heap.update(3, 0)

        # Then
        self.assertEqual(max_heap.heap, [4, 2, 0, 1])

        # Given
        # No need to reset the heap for the second scenario

        # When
        with self.assertRaises(ValueError) as context:
            max_heap.update(5, 10)

        # Then
        self.assertEqual(str(context.exception), "Value old=5 not found in the heap")


if __name__ == '__main__':
    unittest.main()
