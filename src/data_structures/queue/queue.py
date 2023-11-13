class Node:
    """
    Represents a node in the queue.

    Attributes:
        value: The value stored in the node.
        next_node: The next node in the queue.
    """

    def __init__(self, value: int) -> None:
        """
        Initializes a new node with the specified value.

        Args:
            value: The value to store in the node.
        """
        self.value: int = value
        self.next: Node = None

class Queue:
    """
    Implements a queue data structure based on the Node class.

    Attributes:
        front: The node at the front of the queue.
        rear: The node at the rear of the queue.
        size: The number of elements currently in the queue.
    """

    def __init__(self):
        """
        Initializes a new empty queue.
        """
        self.front: Node = None
        self.rear: Node = None
        self.length: int = 0 

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.front is None

    def enqueue(self, value: int) -> None:
        """
        Adds an element to the rear of the queue.

        Args:
            value: The value to add to the queue.
        """
        node = Node(value=value)
        if self.rear is not None:
            self.rear.next = node
        self.rear = node
        if self.front is None:
            self.front = node
        self.length += 1

    def dequeue(self) -> int:
        """
        Removes and returns the element at the front of the queue.

        Returns:
            The value at the front of the queue.
        Raises:
            IndexError: If the queue is empty.
        """
        
        if self.is_empty():
            raise Exception("Queue is empty, dequeue is not possible.")
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.length -= 1
        return node.value

    def size(self) -> int:
        """
        Returns the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return self.length

    def peek(self) -> int:
        """
        Returns the front's data.

        Returns:
            int: The value constains in the front of the queue.
        """
        return self.front.value