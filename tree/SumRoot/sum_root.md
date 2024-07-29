### Problem Statement

Given a binary tree where each node contains a binary digit (0 or 1), compute the sum of all the root-to-leaf paths interpreted as binary numbers.

### High-Level Solution

1. **Tree Traversal**: Perform a depth-first traversal of the binary tree. As you traverse the tree, keep track of the current binary number formed from the root to the current node.
2. **Binary Number Construction**: Update the current binary number by shifting the previous number left (multiply by 2) and adding the current node's value.
3. **Leaf Node Check**: When a leaf node is reached, the current binary number is a complete root-to-leaf path. Add this number to a running total.
4. **Recursive Sum**: Recursively calculate the sum for both left and right subtrees, propagating the current binary number down the tree.
5. **Return Result**: The final sum is the total of all root-to-leaf paths interpreted as binary numbers.

### Function Definition

```python
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def sum_root_to_leaf(tree: TreeNode) -> int:
    # Helper function to calculate the sum of root-to-leaf paths
    def sum_root_to_leaf_helper(tree: TreeNode, partial_path_sum: int = 0) -> int:
        pass  # Implementation here

    return sum_root_to_leaf_helper(tree)
```

### Example Function Calls

```python
# Create a binary tree
#      1
#     / \
#    0   1
#   / \   \
#  0   1   0
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.right = TreeNode(0)

# Calculate the sum of root-to-leaf paths
result = sum_root_to_leaf(root)
print(result)  # Should print the sum of binary numbers represented by root-to-leaf paths
```

This setup provides the problem statement, a high-level solution approach, and the function definition with an example call without giving away the full implementation details.
