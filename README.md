# AVL Tree Operations and Analysis

## Description
This Python script implements an AVL Tree data structure and performs various operations on it, including insertion, deletion, and tree balancing. Additionally, it measures and analyzes the number of operations (assignments and comparisons) for building the tree, OS-SELECT, and OS-DELETE operations.

## AVL Tree Implementation
The AVL tree is implemented using the `AVLNode` and `AVLTree` classes. The AVLTree class provides methods for tree manipulation, including insertion, deletion, balancing, and tree traversal.

## OS-SELECT and OS-DELETE Operations
The script includes implementations for the OS-SELECT and OS-DELETE operations on the AVL tree. OS-SELECT finds the ith smallest key in the tree, and OS-DELETE deletes the ith smallest key from the tree while maintaining balance.

## Analysis and Measurements
The script includes a function `measure_operations` that performs measurements on the AVL tree operations. It generates random values, builds the tree, and performs OS-SELECT and OS-DELETE operations, recording the number of assignments and comparisons.

## Plotting
The script utilizes Matplotlib to visualize the number of operations for building the tree, OS-SELECT, and OS-DELETE across different sizes of the input tree.

## Usage
1. Run the script using a Python interpreter.
2. The AVL tree is created and keys are inserted to create an unbalanced situation.
3. Initial AVL tree is printed using an inorder traversal.
4. Keys are deleted from one side to create imbalance, and the AVL tree is printed again.
5. The script measures and plots the number of operations for building the tree, OS-SELECT, and OS-DELETE.

## Requirements
- Python 3.x
- Matplotlib (install using `pip install matplotlib`)



