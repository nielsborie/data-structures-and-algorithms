import unittest

from src.algorithms.sorting.bubble_sort import BubbleSort

class TestBubbleSort(unittest.TestCase):

    def test_sort_empty_list(self):
        # Given
        input_list = []
        
        # When
        result = BubbleSort.sort(input_list)
        
        # Then
        self.assertEqual(result, [])

    def test_sort_sorted_list(self):
        # Given
        input_list = [1, 2, 3, 4, 5]
        
        # When
        result = BubbleSort.sort(input_list)
        
        # Then
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted_list(self):
        # Given
        input_list = [5, 4, 3, 2, 1]
        
        # When
        result = BubbleSort.sort(input_list)
        
        # Then
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_sort_unsorted_list(self):
        # Given
        input_list = [3, 1, 4, 5, 2]
        
        # When
        result = BubbleSort.sort(input_list)
        
        # Then
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_sort_list_with_duplicates(self):
        # Given
        input_list = [3, 1, 4, 5, 2, 1, 4]
        
        # When
        result = BubbleSort.sort(input_list)
        
        # Then
        self.assertEqual(result, [1, 1, 2, 3, 4, 4, 5])

if __name__ == '__main__':
    unittest.main()
