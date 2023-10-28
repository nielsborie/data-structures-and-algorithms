def swap(array: list[int], left_idx: int, right_idx: int) -> None:
    temp = array[left_idx]
    array[left_idx] = array[right_idx]
    array[right_idx] = temp

def bubble_sort(array: list[int]) -> list[int]:
    last_index: int = len(array)-1
    sorted_flag: bool = False
    while not sorted_flag:
        for index in range(last_index):
            sorted_flag = True
            if array[index]>array[index+1]:
                swap(array=array, left_idx=index, right_idx=index+1)
                sorted_flag = False
        last_index -= 1
    return array

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
  output_1 = bubble_sort(array=input_1)
  check(expected_1, output_1)

  input_2 = [1, 5, 3, 8, 9]
  expected_2 = [1, 3, 5, 8, 9]
  output_2 = bubble_sort(array=input_2)
  check(expected_2, output_2)