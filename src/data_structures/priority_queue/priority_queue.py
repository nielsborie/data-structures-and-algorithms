from src.data_structures.priority_queue.max_heap import MaxHeap


class PriorityQueue:
    def __init__(self):
        self.queue = MaxHeap()

    def enqueue(self, element):
        self.queue.insert(element)

    def peek(self):
        return self.queue.peek()

    def dequeue(self):
        return self.queue.poll()

    def is_empty(self):
        return self.queue.size == 0

    def change_priority_by_index(self, i, new):
        self.queue.update_by_index(i, new)

    def change_priority(self, old, new):
        self.queue.update(old, new)
