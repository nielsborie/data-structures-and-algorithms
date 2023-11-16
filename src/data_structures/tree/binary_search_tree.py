
class Node:
    def __init__(self, value: int) -> None:
        self.left: Node = None
        self.right: Node = None
        self.data: int = value
    
    def insert(self, value: int) -> None:
        if value <= self.data:
            if self.left:
                self.left.insert(value=value)
            else: 
                self.left = Node(value=value)
        else:
            if self.right:
                self.right.insert(value=value)
            else:
                self.right = Node(value=value)

    def contains(self, value: int) -> bool:
        if self.data == value:
            return True
        elif value <= self.data:
            if self.left:
                return self.left.contains(value=value)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(value=value)
            else:
                return False

    def print_in_order(self) -> None:
        # left, self, right
        if self.left:
            self.left.print_in_order()
        print(self.data)
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self) -> None:
        # self, left, right
        print(self.data)
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()

    def print_post_order(self) -> None:
        # left, right, self
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(self.data)


if __name__ == "__main__":
    node = Node(value=10)
    node.insert(5)
    node.insert(8)
    node.insert(15)
    node.print_in_order()