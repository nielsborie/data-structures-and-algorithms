
class Node:
    def __init__(self, value: int) -> None:
        self.left: Node = None
        self.right: Node = None
        self.data: int = value

        self.size: int = 1
        self.min: int = value
        self.max: int = value

    def insert(self, value: int) -> None:
        if value <= self.data:
            if self.left:
                self.left.insert(value=value)
            else: 
                self.left = Node(value=value)
            self.size += 1
            if self.min > value:
                self.min = value
        else:
            if self.right:
                self.right.insert(value=value)
            else:
                self.right = Node(value=value)
            self.size += 1
            self.max = value

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

    def _get_height(self) -> int:
        if self.left and self.right:
            return 1 + max(self.left._get_height(), self.right._get_height())
        elif self.left:
            return 1 + self.left._get_height()
        elif self.right:
            return 1 + self.right._get_height()
        else:
            return 1
        
    # Print nodes at a given level
    def print_at_level(self, level: int) -> None:
        if level == 1:
            print(f"({self.data=}, {self.size=}, {self.min=}, {self.max=})", end=" ")
        elif level > 1:
            # Recursive call
            if self.left:
                self.left.print_at_level(level - 1)
            if self.right:
                self.right.print_at_level(level - 1)
    
    def print_level_order(self) -> None:
        h = self._get_height()
        for i in range(1, h+1):
            self.print_at_level(i)
            print()
            print("-"*10)


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        if self.root:
            self.root.insert(value=value)
        else:
            self.root = Node(value=value)

    def contains(self, value: int) -> bool:
        if self.root:
            return self.root.contains(value=value)
        else: 
            return False
    
    def height(self) -> int:
        if self.root:
            return self.root._get_height()
        else: 
            return 0
        
    def print_in_order(self) -> None:
        if self.root:
            self.root.print_in_order()
    
    def print_level_order(self) -> None:
        if self.root:
            self.root.print_level_order()
        

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    bst.insert(12)
    bst.insert(11)
    bst.insert(13)
    print("In order traversal : ")
    bst.print_in_order()
    print("Level order traversal : ")
    bst.print_level_order()