### Problem Statement
Given a non-empty binary tree, find the maximum path sum. The path may start and end at any node in the tree and must contain at least one node. The path sum is defined as the sum of the node values along the path.

### Function Definition
Here's the function signature for the problem in Python:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    # Implementation here
```

### High-Level Approach
1. **Recursive Calculation**: The core of the solution is a recursive function that computes the maximum gain from each subtree.
2. **Gain Calculation**: For each node, calculate the maximum path sum including the node and its left and/or right subtree gains.
3. **Update Maximum Path**: Keep track of the highest path sum encountered during the traversal.
4. **Return Value**: For each recursive call, return the maximum gain that can be obtained from either the left or right subtree, including the current node's value.

### Example Function Call and Setup
To use the `maxPathSum` function, you first need to create the binary tree and then call the function with the root of the tree.

#### Example
```python
# Constructing the tree:
#       -10
#       /  \
#      9   20
#         /  \
#        15   7

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Finding maximum path sum
result = maxPathSum(root)
print(result)  # Expected output should be the maximum path sum
```

This code will calculate the maximum path sum for the given binary tree using a recursive approach that tracks the maximum sum path at each node.
