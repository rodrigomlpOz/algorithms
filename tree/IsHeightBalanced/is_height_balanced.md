## Problem Statement

Given a binary tree, determine if it is height-balanced. A binary tree is considered height-balanced if the depths of the two subtrees of every node never differ by more than 1.

### Function Signature

```python
def height_balanced(root):
    pass
```

### Input Parameters

- `root`: The root node of the binary tree. Each node is represented by an instance of `TreeNode`, containing the attributes `val` (the value of the node), `left` (the left child), and `right` (the right child).

### Output

- A boolean value indicating whether the tree is height-balanced.

### Example

Consider the following binary tree:

```
      0
     / \
   -3   9
   /   /
 -10  5
```

- **Input:** A reference to the root node of the binary tree.
- **Output:** `True` if the tree is height-balanced, otherwise `False`.

### High-Level Approach

1. **Helper Function `is_balanced`:** This function will recursively determine the height of each subtree and check if it is balanced.
   - If a subtree is `None`, return a height of `-1` and `True` for balanced.
   - Recursively check the left and right subtrees.
   - If either subtree is not balanced, return immediately with `False`.
   - Calculate the height of the current node as `1 + max(left_height, right_height)`.
   - Determine if the current node is balanced by checking if the height difference between the left and right subtrees is no more than 1.
   - Return the current height and a boolean indicating whether the subtree rooted at the current node is balanced.

2. **Main Function `height_balanced`:**
   - Call the `is_balanced` function starting from the root.
   - Return the boolean indicating whether the entire tree is balanced.

This approach ensures that each node is visited once, making the time complexity O(n), where n is the number of nodes in the tree. The function determines balance and height in a single traversal, optimizing the process.
