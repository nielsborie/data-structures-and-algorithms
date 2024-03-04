import threading
import time


def append_value(value, output_array):
    time.sleep(value)
    output_array.append(value)


def sleep_sort(arr):
    output_array = []
    threads = []

    # Create a separate thread for each element in the input array
    for value in arr:
        thread = threading.Thread(target=append_value, args=(value, output_array))
        threads.append(thread)

    # Start the threads
    for thread in threads:
        thread.start()

    # Join the threads to ensure all threads have completed execution
    for thread in threads:
        thread.join()

    return output_array


if __name__ == "__main__":
    unsorted_array = [5, 3, 8, 1, 7]
    sorted_array = sleep_sort(unsorted_array)
    print(sorted_array)
