import random
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.size = 1

def build_tree(n):
    assignments = 0
    comparisons = 0

    def build_tree_recursive(start, end):
        nonlocal assignments, comparisons

        if start > end:
            comparisons += 1
            return None

        mid = (start + end) // 2
        root = Node(mid + 1)
        assignments += 1  # Assignment to root

        root.left = build_tree_recursive(start, mid - 1)
        root.right = build_tree_recursive(mid + 1, end)

        if root.left:
            root.size += root.left.size
            assignments += 1  # Assignment to root.size
        if root.right:
            root.size += root.right.size
            assignments += 1  # Assignment to root.size

        assignments += 2  # Assignments to root.left and root.right

        return root

    root = build_tree_recursive(1, n)
    assignments += 1  # Assignment to root

    return root, assignments, comparisons

def os_select(root, i):
    comparisons = 0
    assignments = 0

    def os_select_recursive(node, index):
        nonlocal comparisons, assignments

        if not node:
            comparisons += 1
            return None

        left_size = node.left.size if node.left else 0
        comparisons += 1  # Comparison for checking if node is None

        if index == left_size + 1:
            comparisons += 1
            return node.key
        elif index <= left_size:
            comparisons += 1
            assignments += 1
            return os_select_recursive(node.left, index)
        else:
            comparisons += 2  # One for the if condition, one for the recursive call
            assignments += 1
            return os_select_recursive(node.right, index - left_size - 1)

    result = os_select_recursive(root, i)

    return result, comparisons, assignments


def os_delete(root, i):
    comparisons = 0
    assignments = 0

    if not root:
        comparisons += 1  # Count the initial comparison
        return None, comparisons, assignments

    left_size = root.left.size if root.left else 0
    comparisons += 1  # Count the comparison for checking if root is None

    if i == left_size + 1:
        comparisons += 1  # Count the comparison for the if condition

        if not root.left:
            assignments += 1
            return root.right, comparisons, assignments
        elif not root.right:
            assignments += 1
            return root.left, comparisons, assignments

        successor, comp, assign = find_min(root.right)
        comparisons += comp
        assignments += assign

        root.key = successor.key
        right_child, comp, assign = os_delete(root.right, 1)
        comparisons += comp
        assignments += assign
        root.right = right_child
    elif i <= left_size:
        comparisons += 1  # Count the comparison for the first if condition
        assignments += 1
        left_child, comp, assign = os_delete(root.left, i)
        comparisons += comp
        assignments += assign
        root.left = left_child
    else:
        comparisons += 2  # Count the comparisons for the first and second if conditions
        assignments += 1
        right_child, comp, assign = os_delete(root.right, i - left_size - 1)
        comparisons += comp
        assignments += assign
        root.right = right_child

    root.size -= 1
    assignments += 1  # Count the assignment for decrementing the size
    return root, comparisons, assignments


def find_min(node, comparisons=0, assignments=0):
    while node.left:
        node = node.left
        comparisons += 1  # Count the comparison in the while loop
    return node, comparisons, assignments


def measure_operations(n):
    build_operations_list = []
    select_operations_list = []
    delete_operations_list = []

    for _ in range(5):
        # Build the tree
        root, build_assignments, build_comparisons = build_tree(n)
        build_operations_list.append(build_assignments + build_comparisons)

        # Perform OS-SELECT and OS-DELETE operations
        select_total_operations = 0
        delete_total_operations = 0

        for i in range(1, n + 1):
            # OS-SELECT
            _, select_comparisons, select_assignments = os_select(root, random.randint(1, i))
            select_total_operations += select_assignments + select_comparisons

            # OS-DELETE
            _, delete_comparisons, delete_assignments = os_delete(root, random.randint(1, i))
            delete_total_operations += delete_assignments + delete_comparisons

        select_operations_list.append(select_total_operations)
        delete_operations_list.append(delete_total_operations)

    return (
        build_operations_list,
        select_operations_list,
        delete_operations_list
    )

def plot_operations(n_values, build_operations, select_operations, delete_operations):
    plt.figure(figsize=(12, 8))
    plt.subplot(3,1,1)
    plt.plot(n_values, delete_operations, label='OS-DELETE', )
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Number of Operations')
    plt.legend()

    plt.subplot(3,1,2)
    plt.plot(n_values, select_operations, label='OS-SELECT', )
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Number of Operations')
    plt.legend()
    
    plt.subplot(3,1,3)
    plt.plot(n_values, build_operations, label='Build Tree',)
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Number of Operations')
    plt.legend()


    plt.tight_layout()
    plt.show()

# Main execution
n_values = list(range(100, 10001, 100))
build_operations_list = []
select_operations_list = []
delete_operations_list = []

for n in n_values:
    build_operations, select_operations, delete_operations = measure_operations(n)

    build_operations_list.append(sum(build_operations) / len(build_operations))
    select_operations_list.append(sum(select_operations) / len(select_operations))
    delete_operations_list.append(sum(delete_operations) / len(delete_operations))

plot_operations(
    n_values, build_operations_list,
    select_operations_list,
    delete_operations_list
)

