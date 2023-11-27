class AVLNode:
    def __init__(self, key):
        """
                 Constructor to initialize the AVLNode with a key
        """
        # Store the key value in the node
        self.key = key

        # Initialize left and right child pointers to None
        self.left = None
        self.right = None

        # Initialize the height of the node to 1
        self.height = 1

        # Initialize the size of the subtree rooted at this node to 1
        self.size = 1

class AVLTree:
    def __init__(self):
        """
         Constructor to initialize an AVLTree with an empty root

        """
        self.root = None
    
    def height(self, node):
        """
             Function to get the height of a node, returns 0 if the node is None

        """
        return node.height if node else 0

    def size(self, node):
        """
             Function to get the size of a node, returns 0 if the node is None

        """
        return node.size if node else 0

    def update_node(self, node):
        """
             Function to update the height and size of a node based on its children

        """
        # Height is 1 plus the maximum height of its left and right children
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        
        # Size is 1 plus the size of its left and right children
        node.size = 1 + self.size(node.left) + self.size(node.right)

    def balance_factor(self, node):
        """
             Function to calculate the balance factor of a node

        """
        # The balance factor is the height of the left subtree minus the height of the right subtree
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        """
             Right rotation operation on the AVL tree

        """
        x = y.left
        T2 = x.right

        # Perform the rotation
        x.right = y
        y.left = T2

        # Update height and size for the rotated nodes
        self.update_node(y)
        self.update_node(x)

        return x

    def left_rotate(self, x):
        """    
             Left rotation operation on the AVL tree
        """
        y = x.right
        T2 = y.left

        # Perform the rotation
        y.left = x
        x.right = T2

        # Update height and size for the rotated nodes
        self.update_node(x)
        self.update_node(y)

        return y

    def insert(self, root, key):
        """
             Insert a new key into the AVL tree
        """
        # Base case: if the root is None, create a new node with the given key
        if not root:
            return AVLNode(key)

        # Recursive insertion based on key comparison
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys are not allowed

        # Update height and size for the current node
        self.update_node(root)

        # Perform rotations to balance the tree
        balance = self.balance_factor(root)

        # Check if the subtree rooted at 'root' is left heavy
        if balance > 1:
            # Check if the key to be inserted is in the left subtree of the left child
            if key < root.left.key:
                # Perform a right rotation to balance the tree
                return self.right_rotate(root)
            else:
                # Perform a left rotation on the left child followed by a right rotation on the root
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        # Check if the subtree rooted at 'root' is right heavy
        if balance < -1:
            # Check if the key to be inserted is in the right subtree of the right child
            if key > root.right.key:
                # Perform a left rotation to balance the tree
                return self.left_rotate(root)
            else:
                # Perform a right rotation on the right child followed by a left rotation on the root
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        # If the subtree is balanced, return the root unchanged
        return root

    def build_tree(self, n):
        """
             Build an AVL tree with keys from 1 to n
        """
        for i in range(1, n + 1):
            self.root = self.insert(self.root, i)

    def os_select(self, root, i):
        """
             OS-Select operation to find the ith smallest key in the tree

        """
        if not root:
            return None

        # Calculate the size of the left subtree + 1 (the root itself)
        left_size = self.size(root.left) + 1

        # Compare i with the size of the left subtree
        if i == left_size:
            return root.key
        elif i < left_size:
            return self.os_select(root.left, i)
        else:
            return self.os_select(root.right, i - left_size)

    def os_delete(self, root, i):

        """
             OS-Delete operation to delete the ith smallest key from the tree
        
        """
        if not root:
            return None

        # Calculate the size of the left subtree + 1 (the root itself)
        left_size = self.size(root.left) + 1

        # Determine which subtree to search for the key to be deleted
        if i < left_size:
            root.left = self.os_delete(root.left, i)
        elif i > left_size:
            root.right = self.os_delete(root.right, i - left_size)
        else:
            # Case 1: Node to be deleted has 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 2: Node to be deleted has 2 children
            else:
                # Find the minimum key in the right subtree
                min_key = self.find_min(root.right).key
                # Replace the current node's key with the minimum key
                root.key = min_key
                # Delete the minimum key from the right subtree
                root.right = self.os_delete(root.right, 1)

        # Update height and size for the current node
        self.update_node(root)

        # Perform rotations to balance the tree
        balance = self.balance_factor(root)

        # Left Heavy
        if balance > 1:
            if self.balance_factor(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        # Right Heavy
        if balance < -1:
            if self.balance_factor(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def find_min(self, root):
        """
             Find the node with the minimum key in the tree

        """
        current = root
        while current.left:
            current = current.left
        return current

    def print_tree(self, root, level=0, prefix="Root: "):
        """
            Recursively print the nodes of a binary tree with indentation.

            Args:
                root (Node): The root of the binary tree.
                level (int): The current level of the tree (used for indentation).
                prefix (str): The prefix to be displayed for the root.

            Returns:
                None
        """
        if root:
            print(" " * (level * 4) + prefix + str(root.key))
            if root.left or root.right:
                self.print_tree(root.left, level + 1, "L--- ")
                self.print_tree(root.right, level + 1, "R--- ")

# Create an AVL tree
avl_tree = AVLTree()

# Insert keys into the AVL tree to create an unbalanced situation
keys_to_insert = [10, 5, 15, 3, 7, 12, 18, 2, 6, 1, 4, 9, 14, 17, 20]
for key in keys_to_insert:
    avl_tree.root = avl_tree.insert(avl_tree.root, key)

# Print the AVL tree before any rotations
print("Inorder Traversal of Initial AVL Tree:")
avl_tree.print_tree(avl_tree.root)
print("\n")

# Delete keys from one side to create imbalance
keys_to_delete = [20, 17, 14, 12, 10, 7, 5, 3, 2, 1]
for key in keys_to_delete:
    avl_tree.root = avl_tree.os_delete(avl_tree.root, key)

# Print the AVL tree after deletions that require rotations
print("Inorder Traversal after Deleting Keys:")
avl_tree.print_tree(avl_tree.root)
