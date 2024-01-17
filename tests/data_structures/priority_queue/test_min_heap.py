import unittest

from src.data_structures.priority_queue.min_heap import MinHeap


class TestMinHeap(unittest.TestCase):

    def test_insert_and_peek(self):
        # Given
        min_heap = MinHeap()

        # When
        min_heap.insert(4)
        min_heap.insert(2)
        min_heap.insert(8)

        # Then
        self.assertEqual(min_heap.peek(), 2)

    def test_poll(self):
        # Given
        min_heap = MinHeap()
        min_heap.insert(4)
        min_heap.insert(2)
        min_heap.insert(8)

        # When
        extracted_value = min_heap.poll()

        # Then
        self.assertEqual(extracted_value, 2)
        self.assertEqual(min_heap.peek(), 4)

    def test_insert_and_poll_empty_heap(self):
        # Given
        min_heap = MinHeap()

        # When
        with self.assertRaises(Exception) as context:
            min_heap.poll()

        # Then
        self.assertEqual(str(context.exception), "Cannot poll a value, the array is empty !")

    def test_peek_empty_heap(self):
        # Given
        min_heap = MinHeap()

        # When
        with self.assertRaises(Exception) as context:
            min_heap.peek()

        # Then
        self.assertEqual(str(context.exception), "Cannot peek a value, the array is empty !")

    def test_insert_and_poll(self):
        # Given
        min_heap = MinHeap()

        # When
        min_heap.insert(4)
        min_heap.insert(2)
        min_heap.insert(8)
        min_heap.insert(1)
        extracted_value = min_heap.poll()

        # Then
        self.assertEqual(extracted_value, 1)
        self.assertEqual(min_heap.peek(), 2)

    def test_multiple_inserts_and_polls(self):
        # Given
        min_heap = MinHeap()

        # When
        min_heap.insert(4)
        min_heap.insert(2)
        min_heap.insert(8)
        min_heap.insert(1)
        min_heap.insert(5)
        extracted_values = [min_heap.poll() for _ in range(min_heap.size)]

        # Then
        expected_values = [1, 2, 4, 5, 8]
        self.assertEqual(extracted_values, expected_values)

if __name__ == '__main__':
    unittest.main()
