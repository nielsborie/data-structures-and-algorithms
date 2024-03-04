from abc import ABC, abstractmethod


class AbstractMergeSort(ABC):

    @abstractmethod
    def merge_sort(self, arr: list[int]) -> list[int]:
        pass


class MergeSortWithReplacement(AbstractMergeSort):
    def merge_sort(self, arr: list[int]) -> list[int]:
        self.merge_sort_helper(arr=arr, left_idx=0, right_idx=len(arr) - 1)

    def mergeback(self, arr: list[int], start_left: int, start_right: int, end_right: int) -> list[int]:
        tmp_arr = [0] * (end_right - start_left + 1)
        left_pointer = start_left
        right_pointer = start_right
        # TODO: check edge cases -> what if there is no more element in left or right side
        for k in range(len(tmp_arr)):
            if right_pointer > end_right or (left_pointer < start_right and arr[left_pointer] <= arr[right_pointer]):
                tmp_arr[k] = arr[left_pointer]
                left_pointer += 1
            else:
                tmp_arr[k] = arr[right_pointer]
                right_pointer += 1
        return tmp_arr

    def copyback(self, arr: list[int], tmp_arr: list[int], offset: int) -> None:
        for k in range(len(tmp_arr)):
            arr[k + offset] = tmp_arr[k]

    def merge_sort_helper(self, arr: list[int], left_idx: int, right_idx: int) -> None:

        if left_idx >= right_idx:
            return

        middle_idx = left_idx + (right_idx - left_idx) // 2
        self.merge_sort_helper(arr=arr, left_idx=left_idx, right_idx=middle_idx)
        self.merge_sort_helper(arr=arr, left_idx=middle_idx + 1, right_idx=right_idx)
        tmp_arr = self.mergeback(arr=arr, start_left=left_idx, start_right=middle_idx + 1, end_right=right_idx)
        self.copyback(arr=arr, tmp_arr=tmp_arr, offset=left_idx)


class MergeSortNoReplacement(AbstractMergeSort):
    def merge_sort(self, arr: list[int]) -> list[int]:

        if len(arr) <= 1:
            return

        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        self.merge_sort(arr=left)
        self.merge_sort(arr=right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


## Merge Sort pseudo code
# Given an array "arr"
# if arr lenght equals to 1, then return arr
# else get the middle index and split the array in two half "left" and "right"
# mergesort(left)
# mergesort(right)
# mergeback(arr, left, right)
#

def copyback(arr, helper, offset):
    for i in range(len(helper)):
        arr[i + offset] = helper[i]


def mergeback(arr, left_start, right_start, right_end):
    helper = [0] * (right_end - left_start + 1)
    left = left_start
    right = right_start
    for index in range(len(helper)):
        if right > right_end or (left < right_start and arr[left] <= arr[right]):
            helper[index] = arr[left]
            left += 1
        else:
            helper[index] = arr[right]
            right += 1
    return helper


def mergesort_helper(arr, left_idx, right_idx):
    if left_idx >= right_idx:
        return

    middle_idx = left_idx + (right_idx - left_idx) // 2
    mergesort_helper(arr, left_idx, middle_idx)
    mergesort_helper(arr, middle_idx + 1, right_idx)
    helper = mergeback(arr, left_idx, middle_idx + 1, right_idx)
    copyback(arr, helper, left_idx)


def merge_sort_wrapper(arr):
    mergesort_helper(arr, 0, len(arr) - 1)


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    input_1 = [100, 200, 300, 400, 500]
    expected_1 = [100, 200, 300, 400, 500]
    merge_sort_wrapper(input_1)
    check(expected_1, input_1)

    input_2 = [1, 5, 3, 8, 9, -1, 88, 56]
    expected_2 = sorted(input_2)
    merge_sort_wrapper(input_2)
    check(expected_2, input_2)
