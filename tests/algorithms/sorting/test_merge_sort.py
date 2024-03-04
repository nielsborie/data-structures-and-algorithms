import unittest
from abc import ABC, abstractmethod

from src.algorithms.sorting.merge_sort import AbstractMergeSort, MergeSortWithReplacement, MergeSortNoReplacement


class AbstractMergeSortTest(ABC):

    @abstractmethod
    def create_merge_sort_instance(self) -> 'AbstractMergeSort':
        pass

    def test_empty_list(self):
        merge_sort = self.create_merge_sort_instance()
        arr = []
        expected = []
        merge_sort.merge_sort(arr)
        self.assertEqual(arr, expected)

    def test_sorted_list(self):
        merge_sort = self.create_merge_sort_instance()
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        merge_sort.merge_sort(arr)
        self.assertEqual(arr, expected)

    def test_reverse_sorted_list(self):
        merge_sort = self.create_merge_sort_instance()
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        merge_sort.merge_sort(arr)
        self.assertEqual(arr, expected)

    def test_duplicate_elements(self):
        merge_sort = self.create_merge_sort_instance()
        arr = [4, 2, 3, 2, 1]
        expected = [1, 2, 2, 3, 4]
        merge_sort.merge_sort(arr)
        self.assertEqual(arr, expected)

    def test_large_list(self):
        merge_sort = self.create_merge_sort_instance()
        arr = [5, 2, 7, 1, 8, 3, 9, 6, 4]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        merge_sort.merge_sort(arr)
        self.assertEqual(arr, expected)


class MergeSortWithReplacementTest(AbstractMergeSortTest, unittest.TestCase):

    def create_merge_sort_instance(self) -> 'AbstractMergeSort':
        return MergeSortWithReplacement()


class MergeSortWithoutReplacementTest(AbstractMergeSortTest, unittest.TestCase):

    def create_merge_sort_instance(self) -> 'AbstractMergeSort':
        return MergeSortNoReplacement()


if __name__ == '__main__':
    unittest.main()
