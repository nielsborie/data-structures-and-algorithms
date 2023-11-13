class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node = None


class Stack:
    """
    empty() - Returns whether the stack is empty - Time Complexity: O(1)
    size() - Returns the size of the stack - Time Complexity: O(1)
    top() / peek() - Returns a reference to the topmost element of the stack - Time Complexity: O(1)
    push(a) - Inserts the element 'a' at the top of the stack - Time Complexity: O(1)
    pop() - Deletes the topmost element of the stack - Time Complexity: O(1)
    """
    def __init__(self) -> None:
        self.top: Node = None
        self.length: int = 0

    def empty(self) -> bool:
        return self.length == 0

    def size(self) -> int:
        return self.length

    def peek(self) -> Node:
        return self.top

    def push(self, a: int) -> None:
        new_node = Node(value=a)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else: 
            self.top = new_node
        self.length += 1

    def pop(self) -> int:
        if self.empty():
            raise Exception("Stack is empty, no value to pop.")
        value = self.top.value
        self.top = self.top.next
        self.length -= 1
        return value