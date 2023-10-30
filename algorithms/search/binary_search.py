# Recursive version
def binary_search_r(arr: list[int], left:int, right: int, target: int):
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

def binary_search_v1(arr: list[int], target: int):
    return binary_search_r(arr=arr, target=target, left=0, right=len(arr)-1)


if __name__== "__main__":
    input_arr = [1, 2, 5, 8, 9]
    target = 2
    print(f"Input array : {input_arr}")
    print(f"Searching the target value : {target}")
    output = binary_search_v1(arr=input_arr, target=target)
    expected = 1
    assert output == expected, f"Expected {expected}, actual {output}"
    print(f"Founded in index : {target}")