## Problem Statement

Given a binary tree, the task is to find the maximum depth of the tree. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Function Signature

```python
def maxDepth(root):
    pass

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Sample binary tree creation
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Call the maxDepth function
maxDepth(root)

```

### Input Parameters

- `root`: The root node of the binary tree. Each node is represented by an instance of `TreeNode`, containing the attributes `val` (the value of the node), `left` (the left child), and `right` (the right child).

### Output

- An integer representing the maximum depth of the binary tree.

### Example

Consider the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```

- **Input:** `root = TreeNode(3)`
  - `root.left = TreeNode(9)`
  - `root.right = TreeNode(20)`
    - `root.right.left = TreeNode(15)`
    - `root.right.right = TreeNode(7)`
- **Output:** `3`

### High-Level Approach

1. **Base Case**: If the `root` is `None`, the tree is empty, and the maximum depth is 0.

2. **Recursive Depth Calculation**:
   - Recursively calculate the depth of the left subtree (`maxDepth(root.left)`).
   - Recursively calculate the depth of the right subtree (`maxDepth(root.right)`).
   - The depth of the current node is `1 + max(left_depth, right_depth)`, where `1` accounts for the current node.

3. **Return Result**: The function returns the maximum depth of the tree by combining the results from the recursive calculations of the left and right subtrees.

This approach ensures that the maximum depth of each subtree is considered, and by recursively traversing the tree, we can determine the overall maximum depth. The time complexity is O(n), where n is the number of nodes in the tree, since each node is visited once.
