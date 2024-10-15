## Problem Statement

The problem involves inverting a binary tree. Inverting a binary tree means swapping the left and right children of all nodes in the tree. The goal is to transform the tree such that the left and right subtrees of every node are swapped.

### Function Signature

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invertTree(root):
    pass
# Creating the tree:
#       4
#      / \
#     2   7
#    / \ / \
#   1  3 6  9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Call invertTree (to be implemented)
invertTree(root)

```

### Input Parameters

- `root`: The root node of the binary tree. Each node is represented by an instance of `TreeNode`, containing the attributes `val` (the value of the node), `left` (the left child), and `right` (the right child).

### Output

- The function should return the root of the inverted binary tree.

### Example

Consider the following binary tree before and after inversion:

**Before Inversion:**

```
    1
   / \
  2   3
 / \ / \
4  5 6  7
```

**After Inversion:**

```
    1
   / \
  3   2
 / \ / \
7  6 5  4
```

### High-Level Approach

1. **Base Case**: If the root is `None`, the function should return `None`. This handles the case of an empty tree or the end of a branch.

2. **Recursive Inversion**:
   - Swap the left and right children of the current node.
   - Recursively invert the left subtree.
   - Recursively invert the right subtree.

3. **Return the Root**: Once all nodes have been processed and the tree has been inverted, return the root of the tree.

This recursive approach ensures that each node's children are swapped, effectively inverting the tree. The function traverses the entire tree, performing the swap operation at each node, and does so in O(n) time complexity where n is the number of nodes in the tree.
