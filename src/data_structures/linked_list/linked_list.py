class Node:
    def __init__(self, data: int = None) -> None:
        self.data: int = data
        self.next: Node = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head: Node = Node()
        
    def append(self, data) -> None:
        node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        
    
    def length(self) -> int:
        current = self.head
        total = 0
        while current.next:
            current = current.next
            total += 1
        return total
    
    def display(self) -> None:
        elems = []
        current = self.head
        while current.next:
            current = current.next
            elems.append(current.data)
        print(elems)
        
    def get(self, index: int) -> int | None:
        if index >= self.length():
            raise IndexError(f"Cannot retrieve element from the LinkedList since its size is {self.length} and the input index is {index}")
        current = self.head
        cur_idx = 0
        while True:
            current = current.next
            if cur_idx==index:
                return current.data
            cur_idx += 1
            
    def delete(self, index: int) -> None:
        if index >= self.length():
            raise IndexError(f"Cannot delete element from the LinkedList since its size is {self.length} and the input index is {index}")
        current = self.head
        cur_idx = 0
        while True:
            previous = current
            current = current.next
            if cur_idx==index:
                previous.next = current.next
                break
            cur_idx += 1
        
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.display()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.display()
    
    print(f"{linked_list.get(2)=}")
    linked_list.delete(2)
    linked_list.display()
    print(f"{linked_list.get(2)=}")
    