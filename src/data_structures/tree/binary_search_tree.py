
from collections import deque


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

    def _get_max_depth(self):
        """Find the max depth in that Tree

        Time complexity : O(N)
        Space complexity : O(N) at worst
        """
        if self.left and self.right:
            return 1 + max(self.left._get_max_depth(), self.right._get_max_depth())
        elif self.left:
            return 1 + self.left._get_max_depth()
        elif self.right:
            return 1 + self.right._get_max_depth()
        else:
            return 1

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
    
    def get_height_recursive(self):
        """Get the height of that Tree

        Implementation using recursion.

        Time complexity : O(N)
        Space complexity : O(N) at worst
        """
        if self.root:
            return self.root._get_max_depth()
        else:
            return 0

    def get_height_breadth_first_search(self):
        """Get the height of that Tree

        Implementation using BFS.

        Time complexity : O(N)
        Space complexity : O(N) at worst
        """
        if not self.root:
            return 0
        
        level = 0
        q = deque([self.root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    

    def get_height_depth_first_search(self):
        """Get the height of that Tree

        Implementation using DFS.

        Time complexity : O(N)
        Space complexity : O(N) at worst
        """
        if not self.root:
            return 0
        
        level = 1
        stack = [(self.root, 1)]
        while stack:
            node, depth = stack.pop()
            if node:
                level = max(level, depth)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return level


    
    def print_in_order(self) -> None:
        if self.root:
            self.root.print_in_order()
    
    def print_post_order(self) -> None:
        if self.root:
            self.root.print_post_order()
        
    def print_pre_order(self) -> None:
        if self.root:
            self.root.print_pre_order()
        

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(1)
    bst.insert(5)
    bst.insert(15)
    bst.insert(8)
    print("In order :")
    bst.print_in_order()
    print("Post order :")
    bst.print_post_order()
    print("Pre order :")
    bst.print_pre_order()
    print(f"Height of the Tree [recursive version] : {bst.get_height_recursive()=}")
    print(f"Height of the Tree [BFS version]: {bst.get_height_breadth_first_search()=}")
    print(f"Height of the Tree [DFS version]: {bst.get_height_depth_first_search()=}")