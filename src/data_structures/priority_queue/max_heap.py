class MaxHeap:
    def __init__(self) -> None:
        self.heap: list[int] = []
        self.size: int = 0
    
    def has_left(self, i: int) -> bool:
        return self.left(i) < len(self.heap)
    
    def left(self, i: int) -> int:
        return 2*i + 1

    def has_right(self, i: int) -> bool:
        return self.right(i) < len(self.heap)

    def right(self, i: int) -> int:
        return 2*i + 2

    def has_parent(self, i: int) -> bool:
        return self.parent(i) >= 0

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def heapify_up(self, i: int) -> None:
        while self.has_parent(i) and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify_down(self, i: int) -> None:
        while (self.has_left(i) and self.heap[i] < self.heap[self.left(i)]) or (self.has_right(i) and self.heap[i] < self.heap[self.right(i)]):
            greater = self.left(i) if not self.has_right(i) or self.heap[self.left(i)] > self.heap[self.right(i)] else self.right(i)
            self.heap[i], self.heap[greater] = self.heap[greater], self.heap[i]
            i = greater

    def insert(self, val: int) -> None:
        self.heap.append(val)
        self.size += 1
        self.heapify_up(self.size - 1)

    def poll(self) -> int:
        if not self.heap:
            raise Exception("Cannot poll a value on an empty heap.")
        max_val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.size -= 1
        self.heapify_down(0)
        return max_val

    def peek(self) -> int:
        if not self.heap:
            raise Exception("Cannot peek a value on an empty heap.")
        return self.heap[0]

    def update(self, old: int, new: int) -> None:
        if old not in self.heap:
            raise ValueError(f"Value {old=} not found in the heap")
        self.update_by_index(self.heap.index(old), new)

    def update_by_index(self, i: int, new: int) -> None:
        if i >= self.size:
            raise IndexError(f"You're trying to update a non existing index; received {i=} but the heap has only {self.size} elements.")
        old = self.heap[i]
        self.heap[i] = new
        if old > new:
            self.heapify_up(i)