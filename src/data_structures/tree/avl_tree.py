# Python code to insert a node in AVL tree 

# Generic tree node class 

class AVLTreeNode(object): 
	def __init__(self, val: int): 
		self.val: int = val 
		self.left: AVLTreeNode = None
		self.right: AVLTreeNode = None
		self.height: int = 1

# AVL tree class which supports the 
# Insert operation 
class AVLTree(object):
	# Recursive function to insert key in 
	# subtree rooted with node and returns 
	# new root of subtree. 
	def insert(self, root: AVLTreeNode, key: int) -> AVLTreeNode:
		# Step 1: perform a basic insert
		if not root:
			return AVLTreeNode(val=key)
		if key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)
		
		# Step 2: Update the height
		root.height = self.compute_height(root)

		# Step 3: Get the balance
		balance = self.get_balance(root)

		# Step 4 - If the node is unbalanced,  
		# then try out the 4 cases 
		# Case 1 - Left Left
		if balance > 1 and key < root.left.val:
			return self.right_rotate(root)

		# Case 2 - Left Right
		if balance > 1 and key > root.left.val:
			root.left = self.left_rotate(root.left)
			return self.right_rotate(root)
		
		# Case 3 - Right Right
		if balance < -1 and key > root.right.val:
			return self.left_rotate(root)
		
		# Case 4 - Right Left
		if balance < -1 and key < root.right.val:
			root.right = self.right_rotate(root.right)
			return self.left_rotate(root)
		
		# Otherwise, if the tree is already balanced, return the root
		return root

	def left_rotate(self, root: AVLTreeNode) -> AVLTreeNode:
		"""
		T1, T2 and T3 are subtrees of the tree, rooted with y (on the left side) or x (on the right side)     
      
		     y                               x
		    / \     Right Rotation (y)      /  \
		   x   T3   - - - - - - - >        T1   y 
		  / \       < - - - - - - -            / \
		 T1  T2     Left Rotation  (x)       T2  T3

		Keys in both of the above trees follow the following order 
		keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
		So BST property is not violated anywhere.
        """
		x = root
		y = x.right
		T2 = y.left

		x.right = T2
		y.left = x

		# Update heights
		x.height = self.compute_height(x)
		y.height = self.compute_height(y)
        
        # Return the new root
		return y
	

	def right_rotate(self, root: AVLTreeNode) -> AVLTreeNode:
		"""
		T1, T2 and T3 are subtrees of the tree, rooted with y (on the left side) or x (on the right side)     
      
		     y                               x
		    / \     Right Rotation (y)      /  \
		   x   T3   - - - - - - - >        T1   y 
		  / \       < - - - - - - -            / \
		 T1  T2     Left Rotation  (x)       T2  T3

		Keys in both of the above trees follow the following order 
		keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
		So BST property is not violated anywhere.
        """
		y = root
		x = y.left
		T2 = x.right

		y.left = T2
		x.right = y

		# Update heights
		x.height = self.compute_height(x)
		y.height = self.compute_height(y)

		# Return the new root
		return x


	def get_height(self, root: AVLTreeNode)-> int:
		if not root:
			return 0
		return root.height
	
	def compute_height(self, root: AVLTreeNode)-> int:
		return 1 + max(self.get_height(root.left), self.get_height(root.right))
	
	def get_balance(self, root: AVLTreeNode) -> int:
		if not root:
			return 0
		return self.get_height(root.left) - self.get_height(root.right)


### Original class
class AVL_Tree(object):
	# Recursive function to insert key in 
	# subtree rooted with node and returns 
	# new root of subtree. 
	def insert(self, root: AVLTreeNode, key: int):

		# Step 1 - Perform normal BST 
		if not root:
			return AVLTreeNode(key)
		if key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)
		
		# Step 2 - Update the height of the ancestor node 
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

		# Step 3 - get the balance factor
		balance = self.getBalance(root)
		
		# Step 4 - If the node is unbalanced,  
		# then try out the 4 cases 
		# Case 1 - Left Left
		if balance > 1 and key < root.left.val:
			return self.rightRotate(root)
		
		# Case 2 - Right Right
		if balance < -1 and key > root.right.val:
			return self.leftRotate(root)
		
		# Case 3 - Left Right
		if balance > 1 and key > root.left.val: 
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)
		
		# Case 4 - Right Left 
		if balance < -1 and key < root.right.val:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root) 
		
		return root 

	def leftRotate(self, z: AVLTreeNode):
		"""
        T1, T2 and T3 are subtrees of the tree, rooted with y (on the left side) or x (on the right side)     

             y                               x
            / \     Right Rotation          /  \
           x   T3   - - - - - - - >        T1   y 
          / \       < - - - - - - -            / \
         T1  T2     Left Rotation            T2  T3
 
        Keys in both of the above trees follow the following order 
        keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
        So BST property is not violated anywhere.
        """
		y = z.right
		T2 = y.left

        # Rotate
		y.left = z
		z.right = T2
		
        # Update heights
		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        # Return the new root
		return y

	def rightRotate(self, z: AVLTreeNode):
		y = z.left
		T2 = y.right
		
        # Rotate
		y.right = z
		z.left = T2
		
        # Update heights
		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
		
        # Return the new root
		return y 
	def getHeight(self, root: AVLTreeNode): 
		if not root:
			return 0
		return root.height

	def getBalance(self, root: AVLTreeNode): 
		if not root:
			return 0
		return (self.getHeight(root.left) - self.getHeight(root.right))

	def preOrder(self, root: AVLTreeNode): 
		if not root: 
			return
		print("{0} ".format(root.val), end="") 
		self.preOrder(root.left) 
		self.preOrder(root.right) 


if __name__ == "__main__":
	myTree = AVLTree()
	root = None
	root = myTree.insert(root, 10)
	root = myTree.insert(root, 20)
	root = myTree.insert(root, 30)
	root = myTree.insert(root, 40)
	root = myTree.insert(root, 50)
	root = myTree.insert(root, 25)
	# Preorder Traversal
	print("Preorder traversal of the", "constructed AVL tree is")
	myTree.preOrder(root)
	print()
