# Recursive version
def binary_search_r(arr: list[int], left:int, right: int, target: int) -> int:
    if left >= right:
        return -1
    else:
        middle = left + (right - left) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            return binary_search_r(arr=arr, left=left, right=middle, target=target)
        else:
            return binary_search_r(arr=arr, left=middle+1, right=right, target=target)

def binary_search_v1(arr: list[int], target: int) -> int:
    return binary_search_r(arr=arr, target=target, left=0, right=len(arr)-1)

# Iterative
def binary_search_it(arr: list[int], target: int) -> int:
    left_idx = 0
    right_idx = len(arr)-1
    while left_idx < right_idx:
        middle_idx = left_idx + (right_idx - left_idx)//2
        if arr[middle_idx] == target:
            return middle_idx
        elif arr[middle_idx] < target:
            left_idx = middle_idx + 1
        else:
            right_idx = middle_idx
    return -1

if __name__== "__main__":
    input_arr = [1, 2, 5, 8, 9]
    target = 2
    print(f"Input array : {input_arr}")
    print(f"Searching the target value : {target}")
    output = binary_search_it(arr=input_arr, target=target)
    expected = 1
    assert output == expected, f"Expected {expected}, actual {output}"
    print(f"Founded in index : {output}")