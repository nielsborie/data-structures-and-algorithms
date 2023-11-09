import unittest
from abc import ABC, abstractmethod
import sys
import inspect


class AbstractBinarySearch(ABC):

    @abstractmethod
    def binary_search(self, arr: list[int], x: int):
        pass


class BinarySearchRecursiveVersion(AbstractBinarySearch):
    def binary_search(self, arr: list[int], x: int):
        if not arr:
            return -1
        return self.binary_search_helper(arr=arr, target=x, left_pointer=0, right_pointer=len(arr)-1)

    def binary_search_helper(self, arr: list[int], target: int, left_pointer: int, right_pointer):
        if left_pointer > right_pointer:
            return -1
        middle_pointer = left_pointer + (right_pointer - left_pointer) // 2
        if arr[middle_pointer] == target:
            return middle_pointer
        elif arr[middle_pointer] > target:
            return self.binary_search_helper(arr=arr, target=target, left_pointer=left_pointer, right_pointer=middle_pointer - 1)
        else: 
            return self.binary_search_helper(arr=arr, target=target, left_pointer=middle_pointer + 1, right_pointer=right_pointer)
        


class BinarySearchIterativeVersion(AbstractBinarySearch):
    def binary_search(self, arr: list[int], x: int):
        if not arr:
            return -1
        
        left_idx = 0
        right_idx = len(arr) - 1
        
        while left_idx <= right_idx:
            middle_index = left_idx + (right_idx - left_idx) // 2
            if arr[middle_index] == x:
                return middle_index
            elif arr[middle_index] > x:
                right_idx = middle_index - 1
            else: 
                left_idx = middle_index + 1
        return -1