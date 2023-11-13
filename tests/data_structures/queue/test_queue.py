import unittest

from src.data_structures.queue.queue import Queue

class TestQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        # Given an empty queue
        queue = Queue()

        # When enqueueing and dequeueing elements
        queue.enqueue(1)
        dequeued_value = queue.dequeue()

        # Then the dequeued value should be equal to the enqueued value
        self.assertEqual(dequeued_value, 1)

        # Given a queue with multiple elements
        queue.enqueue(2)
        queue.enqueue(3)

        # When dequeueing multiple elements
        dequeued_value1 = queue.dequeue()
        dequeued_value2 = queue.dequeue()

        # Then the dequeued values should match the enqueued order
        self.assertEqual(dequeued_value1, 2)
        self.assertEqual(dequeued_value2, 3)

    def test_is_empty(self):
        # Given an empty queue
        queue = Queue()

        # When checking if the queue is empty
        is_empty_before_enqueue = queue.is_empty()

        # Then the queue should be empty initially
        self.assertTrue(is_empty_before_enqueue)

        # When enqueueing an element
        queue.enqueue(1)

        # Then the queue should not be empty after enqueue
        is_empty_after_enqueue = queue.is_empty()
        self.assertFalse(is_empty_after_enqueue)

        # When dequeueing the element
        queue.dequeue()

        # Then the queue should be empty after dequeue
        is_empty_after_dequeue = queue.is_empty()
        self.assertTrue(is_empty_after_dequeue)

    def test_size(self):
        # Given an empty queue
        queue = Queue()

        # When getting the size of the queue
        size_before_enqueue = queue.size()

        # Then the size should be 0 initially
        self.assertEqual(size_before_enqueue, 0)

        # When enqueueing an element
        queue.enqueue(1)

        # Then the size should be 1 after enqueue
        size_after_enqueue = queue.size()
        self.assertEqual(size_after_enqueue, 1)

        # When dequeueing the element
        queue.dequeue()

        # Then the size should be 0 after dequeue
        size_after_dequeue = queue.size()
        self.assertEqual(size_after_dequeue, 0)

        # Given a queue with multiple elements
        queue.enqueue(2)
        queue.enqueue(3)

        # When getting the size with multiple elements
        size_with_multiple_elements = queue.size()

        # Then the size should match the number of elements
        self.assertEqual(size_with_multiple_elements, 2)

    def test_dequeue_empty_queue(self):
        # Given an empty queue
        queue = Queue()

        # When trying to dequeue from an empty queue
        with self.assertRaises(Exception):
            queue.dequeue()

    def test_enqueue_dequeue_large_scale(self):
        # Given an empty queue
        queue = Queue()

        # When enqueueing a large number of elements
        for i in range(1000):
            queue.enqueue(i)

        # Then the size should be equal to the number of enqueued elements
        self.assertEqual(queue.size(), 1000)

        # When dequeueing the elements
        for i in range(1000):
            dequeued_value = queue.dequeue()

            # Then the dequeued value should match the enqueued order
            self.assertEqual(dequeued_value, i)

        # Then the queue should be empty after dequeueing all elements
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)

if __name__ == '__main__':
    unittest.main()
