from src.data_structures.tree.binary_search_tree import BinarySearchTree, TreeNode

def bst_to_array(node: TreeNode, nodes: list[TreeNode]) -> None:
    """Convert a BST to a sorted array.

    Traverse the BST in-order (left -> root -> right) and store it into the array.

    Args:
        node (TreeNode): root node of the BST

    Returns:
        None : this function mutate in place the array 'keys'

    Time complexity : O(N)
    Space complexity : O(N)
    """
    if node is None:
        return
    bst_to_array(node=node.left, nodes=nodes)
    nodes.append(node)
    bst_to_array(node=node.right, nodes=nodes) 

def balance_tree_util(nodes: list[TreeNode], left_idx: int, right_idx: int) -> TreeNode:
    
    if left_idx > right_idx:
        return
    
    middle_idx = left_idx + (right_idx - left_idx)//2
    node = nodes[middle_idx]
    node.left = balance_tree_util(nodes=nodes, left_idx=left_idx, right_idx=middle_idx-1)
    node.right = balance_tree_util(nodes=nodes, left_idx=middle_idx+1, right_idx=right_idx)
    return node
    


def balance_tree(root: TreeNode) -> TreeNode:
    """Function to balance a BST
    The idea here is to iterate (in order) through all existing nodes in the BST -> this will return a sorted array.

    Then recursively do this :
    - find the middle value of the array, put it as the current root
    - apply this logic to the left subarray to find the left successor of the current root
    - apply this logic to the right subarray to find the right successor of the current root

    return the first root

    Args:
        node (TreeNode): node of a BST

    Returns:
        TreeNode: the root node of the newly created balanced BST

    Time Complexity: O(n), As we are just traversing the tree twice. Once in inorder traversal and then in construction of the balanced tree.
    Auxiliary space: O(n), The extra space is used to store the nodes of the inorder traversal in the vector. Also the extra space taken by recursion call stack is O(h) where h is the height of the tree.
    """
    sorted_nodes = []
    bst_to_array(node=root, nodes=sorted_nodes)

    return balance_tree_util(nodes=sorted_nodes, left_idx=0, right_idx=len(sorted_nodes)-1)

def height(root):
 
    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def is_balanced(root: TreeNode):
 
    # Base condition
    if root is None:
        return True
 
    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)
 
    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and is_balanced(root.left) is True and is_balanced(root.right) is True:
        return True


if __name__=="__main__":
    """
    
    Input:
       30
      /
     20
    /
   10
    Output:
        20
    /   \
    10     30


    Input:
            4
            /
        3
        /
        2
        /
    1
    Output:
        3            3           2
        /  \         /  \        /  \
    1    4   OR  2    4  OR  1    3   OR ..
        \          /                   \
        2        1                     4 

    Input:
            4
            /   \
        3     5
        /       \
        2         6 
        /           \
    1             7
    Output:
        4
        /    \
    2      6
    /  \    /  \
    1    3  5    7 

    """
    # Case 1
    bst1 = BinarySearchTree()
    bst1.insert(30)
    bst1.insert(20)
    bst1.insert(10)
    print("# 1 - Unbalanced Tree : ")
    bst1.print_level_order()
    print("# 1 - Balanced Tree : ")
    balanced_bst1 = balance_tree(root=bst1.root)
    balanced_bst1.print_level_order()

    # Case 2
    bst1 = BinarySearchTree()
    bst1.insert(4)
    bst1.insert(3)
    bst1.insert(2)
    bst1.insert(1)
    print("# 2 - Unbalanced Tree : ")
    bst1.print_level_order()
    print("# 2 - Balanced Tree : ")
    balanced_bst1 = balance_tree(root=bst1.root)
    balanced_bst1.print_level_order()

    # Case 3
    bst1 = BinarySearchTree()
    bst1.insert(4)
    bst1.insert(3)
    bst1.insert(2)
    bst1.insert(1)
    bst1.insert(5)
    bst1.insert(6)
    bst1.insert(7)
    print("# 3 - Unbalanced Tree : ")
    bst1.print_level_order()
    print("# 3 - Balanced Tree : ")
    balanced_bst1 = balance_tree(root=bst1.root)
    balanced_bst1.print_level_order()