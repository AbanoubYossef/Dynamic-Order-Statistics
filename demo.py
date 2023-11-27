import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

def build_tree(n):
    def build_tree_recursive(start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        root = Node(mid + 1)

        root.left = build_tree_recursive(start, mid - 1)
        root.right = build_tree_recursive(mid + 1, end)

        if root.left:
            root.size += root.left.size
        if root.right:
            root.size += root.right.size

        return root

    return build_tree_recursive(1, n)

def os_select(root, i):
    if not root:
        return None

    left_size = root.left.size if root.left else 0
    if i == left_size + 1:
        return root.key
    elif i <= left_size:
        return os_select(root.left, i)
    else:
        return os_select(root.right, i - left_size - 1)


def find_min(node):
    while node.left:
        node = node.left
    return node

def os_delete(root, i):
    if not root:
        return None

    left_size = root.left.size if root.left else 0

    if i == left_size + 1:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        successor = find_min(root.right)
        root.key = successor.key
        root.right = os_delete(root.right, 1)
    elif i <= left_size:
        root.left = os_delete(root.left, i)
    else:
        root.right = os_delete(root.right, i - left_size - 1)

    root.size -= 1
    return root


def print_tree(root, level=0, prefix="Root: "):
    """
    Recursively print the nodes of a binary tree with indentation.

    Args:
        root (Node): The root of the binary tree.
        level (int): The current level of the tree (used for indentation).
        prefix (str): The prefix to be displayed for the root.

    Returns:
        None
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.key) + f" (Size: {root.size})")

        # Check if the node has children before recursively calling
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L --- ")
            if root.right:
                print_tree(root.right, level + 1, "R --- ")
        else:
            # Indicate when the node has no children
            print(" " * ((level + 1) * 4) + "No children")

# Demonstrate the algorithm with a small input (n=11)
n_demo = 11
bst_root_demo = build_tree(n_demo)

print("Initially Built Tree:")
print_tree(bst_root_demo)
print("\n")

indices_to_select_demo = [3, 6, 9]
for i in indices_to_select_demo:
    selected_element_demo = os_select(bst_root_demo, i)
    print(f"OS-SELECT for i={i}: {selected_element_demo}")

element_to_delete_demo = 5
bst_root_demo = os_delete(bst_root_demo, element_to_delete_demo)

print(f"\nAfter OS-DELETE({element_to_delete_demo}):")
print_tree(bst_root_demo)
