class MinHeap:
    def __init__(self) -> None:
        self.size: int = 0
        self.array: list[int] = []

    def has_parent(self, index: int) -> bool:
        return self.get_parent_index(child_index=index) >= 0 
    
    def has_left_child_index(self, index: int) -> bool:
        return self.get_left_child_index(parent_index=index) < len(self.array)

    def has_right_child_index(self, index: int) -> bool:
        return self.get_right_child_index(parent_index=index) < len(self.array)
    
    def get_parent_index(self, child_index: int) -> int:
        return (child_index - 1)//2
    
    def get_left_child_index(self, parent_index: int) -> int:
        return 2*parent_index + 1
    
    def get_right_child_index(self, parent_index: int) -> int:
        return 2*parent_index + 2

    def parent(self, index: int) -> int:
        return self.array[self.get_parent_index(child_index=index)]

    def left(self, index: int) -> int:
        return self.array[self.get_left_child_index(parent_index=index)]

    def right(self, index: int) -> int:
        return self.array[self.get_right_child_index(parent_index=index)]

    def heapify_down(self, index: int) -> None:
        while self.has_left_child_index(index=index):
            smaller_child = self.get_left_child_index(parent_index=index)
            if self.has_right_child_index(index=index) and self.right(index=index) < self.left(index=index):
                smaller_child = self.get_right_child_index(parent_index=index)
            
            if self.array[index] <= self.array[smaller_child]:
                break
            else:
                self.swap(index_1=index, index_2=smaller_child)
            index = smaller_child
        
    
    def heapify_up(self, index: int) -> None:
        while self.has_parent(index=index) and self.parent(index=index) >= self.array[index]:
            self.swap(index_1=self.get_parent_index(child_index=index), index_2=index)
            index = self.get_parent_index(child_index=index)

    def swap(self, index_1: int, index_2: int) -> None:
        self.array[index_1], self.array[index_2] = self.array[index_2], self.array[index_1]

    def peek(self) -> int:
        if not self.array:
            raise IndexError(f"Cannot peek a value, the array is empty !")
        return self.array[0]
        
    def poll(self) -> int:
        if not self.array:
            raise IndexError(f"Cannot poll a value, the array is empty !")
        
        min_value = self.array[0]
        last_value = self.array.pop()
        self.size -= 1

        if self.array:
            self.array[0] = last_value
            self.heapify_down(index=0)
        return min_value
    
    def insert(self, value: int) -> None:
        self.array.append(value)
        self.size += 1
        self.heapify_up(index=len(self.array) - 1)

    def update_by_index(self, i: int, new: int):
        if i >= self.size:
            raise IndexError(f"You're trying to update a non existing index; received {i=} but the heap has only {self.size} elements.")
        old = self.array[i]
        self.array[i] = new
        if new < old:
            self.heapify_up(i)
        else:
            self.heapify_down(i)

    def update(self, old: int, new: int):
        if old in self.array:
            self.update_by_index(self.array.index(old), new) 
        else:
            raise ValueError(f"Value {old=} not found in the heap")

if __name__ == "__main__":
    # Exemple d'utilisation
    min_heap = MinHeap()
    min_heap.insert(4)
    min_heap.insert(2)
    min_heap.insert(8)
    min_heap.insert(1)
    print(f"Peek the minimum value in the MinHeap : {min_heap.peek()=}")
    print(f"- Extracting minimum value from the MinHeap ...")
    minimum = min_heap.poll()
    print(f"Minimum value extracted : {minimum=}")
    print(f"Peek the minimum value in the MinHeap : {min_heap.peek()=}")


