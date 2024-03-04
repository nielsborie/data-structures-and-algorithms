class BubbleSort:
    @staticmethod
    def sort(array: list[int]) -> list[int]:
        last_index = len(array) - 1

        while last_index > 0:
            sorted_flag = True

            for i in range(last_index):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    sorted_flag = False

            if sorted_flag:
                break

            last_index -= 1

        return array
