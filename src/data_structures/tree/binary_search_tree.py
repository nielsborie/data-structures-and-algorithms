
from collections import deque


class TreeNode:
    def __init__(self, value: int) -> None:
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.data: int = value
    
    def insert(self, value: int) -> None:
        if value <= self.data:
            if self.left:
                self.left.insert(value=value)
            else: 
                self.left = TreeNode(value=value)
        else:
            if self.right:
                self.right.insert(value=value)
            else:
                self.right = TreeNode(value=value)

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

    def _print_at_given_level(self, level: int) -> None:
        """
        Recursively prints nodes at the given level of the tree.

        Args:
            level (int): The level of the tree to print.

        Time Complexity:
            O(n), where n is the number of nodes in the tree.

        Returns:
            None
        """
        if level == 1:
            print(f"({self.data})" , end=" ")
        elif level > 1:
            if self.left:
                self.left._print_at_given_level(level=level-1)
            if self.right:
                self.right._print_at_given_level(level=level-1)

    def print_level_order(self) -> None:
        """
        Prints the values of the tree in level order.

        Uses Breadth-First Search (BFS) to traverse the tree layer by layer.

        Time Complexity:
            O(n), where n is the number of nodes in the tree.

        Space Complexity:
            O(n), where n is the number of nodes in the tree.

        Returns:
            None
        """
        h = self._get_max_depth()
        for i in range(1, h+1):
            self._print_at_given_level(i)
            print()
            print("-"*30)
        

    def delete_node(self, node_to_delete: int):
        """
        Delete a node with the specified key from the subtree rooted at this node.

        This method recursively searches for the node with the specified key and performs the deletion.
        The deletion follows the rules of a binary search tree:
        - If the node to delete has no child or only one child, it is simply removed.
        - If the node to delete has two children, it is replaced by its successor, and the successor is then deleted.

        Time Complexity:
            The time complexity of the delete_node method is O(h), where h is the height of the subtree rooted at the current node.
            - In the worst case, when the tree is unbalanced (skewed), the height h is equal to the number of nodes in the tree (n). Therefore, the worst-case time complexity becomes O(n).
            - In the best case, when the tree is balanced, the height h is logarithmic in the number of nodes (log(n)), resulting in a best-case time complexity of O(log(n)).
            - The time complexity depends on the depth of the tree and the efficiency of the tree balancing.

        Space Complexity:
            The space complexity of the delete_node method is O(h), where h is the height of the recursive call stack.
            - In the worst case, when the tree is unbalanced (skewed), the height h is equal to the number of nodes in the tree (n). Therefore, the worst-case space complexity becomes O(n).
            - In the best case, when the tree is balanced, the height h is logarithmic in the number of nodes (log(n)), resulting in a best-case space complexity of O(log(n)).
            - The space complexity is determined by the maximum depth of the recursive call stack during the method's execution.

        It's important to note that these complexities are specific to the delete_node method and may vary based on the structure of the binary search tree (balanced or unbalanced). Additionally, the space complexity can be reduced by using an iterative approach instead of recursion.

        Args:
            key: The key of the node to delete.

        Returns:
            TreeNode: The root of the subtree after the deletion.
        """
        
        if self is None:
            return self
        
        if node_to_delete < self.data:
            if self.left is not None:
                self.left = self.left.delete_node(node_to_delete=node_to_delete)
        elif node_to_delete > self.data:
            if self.right is not None:
                self.right = self.right.delete_node(node_to_delete=node_to_delete)
        else:
            # We found the node to delete

            # Case 1: No child or one child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # Case 2: Two children, replace with successor
            # The idea is to take the minium value on the right subtree and replace the current node with it, then recursively delete this new value on the right subtree
            successor: TreeNode = self._find_min_child(self.right)
            self.data = successor.data
            self.right = self.right.delete_node(node_to_delete=successor.data)
        return self
    
    def _find_min_child(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
# Function alternative
def delete_node(root: TreeNode, key: int):
    if root is None:
        return root
    
    if key > root.data:
        root.right = delete_node(root=root.right, key=key)
    elif key < root.data:
        root.left = delete_node(root=root.left, key=key)
    else:
        # Found the node to delete

        # Case 1 : No child or one child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            successor = find_min_value(node=root.right)
            root.data = successor.data
            root.right = delete_node(root=root.right, key=successor.data)
    return root

def find_min_value(node: TreeNode):
    current = node
    while current.left:
        current = current.left
    return current

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        if self.root:
            self.root.insert(value=value)
        else:
            self.root = TreeNode(value=value)

    def contains(self, value: int) -> bool:
        if self.root:
            return self.root.contains(value=value)
        else: 
            return False
        
    def delete_node(self, to_delete: int):
        if self.root:
            return self.root.delete_node(node_to_delete=to_delete)
    
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
        
    def print_level_order(self) -> None:
        if self.root:
            self.root.print_level_order()

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