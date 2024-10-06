## Problem Statement: Path Sum

Given a binary tree and a target sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

A leaf is a node with no children.

### Function Signature

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_sum(tree: TreeNode, remaining_weight: int) -> bool:
    pass

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

# Check if there is a path with the sum 22
result = has_path_sum(root, 22)
print(result)  # Output: True

# Check if there is a path with the sum 27
result = has_path_sum(root, 27)
print(result)  # Output: True

# Check if there is a path with the sum 26
result = has_path_sum(root, 26)
print(result)  # Output: False
```

### Approach

The problem requires checking if there exists a root-to-leaf path in a binary tree where the sum of the node values equals a given number. The function `has_path_sum` can solve this problem using a recursive depth-first search approach:

1. **Base Case:** If the current node (`tree`) is `None`, it means we've reached a non-existent node (beyond a leaf), so we return `False`.
2. **Leaf Node Check:** If the current node is a leaf (it has no left or right children), check if its value equals the remaining sum (`remaining_weight`). If yes, return `True`; otherwise, return `False`.
3. **Recursive Case:** If the current node is not a leaf, subtract the current node's value from the remaining weight and recursively check both the left and right subtrees to see if either contains a path that matches the updated sum.

This recursive approach ensures that all paths from the root to the leaves are checked.
```

### Example Usage

```python
# Example tree construction
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \      \
#  7    2      1

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

# Check if there is a path with the sum 22
result = has_path_sum(root, 22)
print(result)  # Output: True

# Check if there is a path with the sum 27
result = has_path_sum(root, 27)
print(result)  # Output: True

# Check if there is a path with the sum 26
result = has_path_sum(root, 26)
print(result)  # Output: False
```

### Explanation

- **Base Case Handling:** The function handles the case where the tree is empty (`tree` is `None`) by returning `False`.
- **Leaf Node Condition:** When a leaf node is encountered, the function checks if the path sum equals the target sum (`remaining_weight`).
- **Recursion:** For non-leaf nodes, the function recursively checks the left and right subtrees, updating the `remaining_weight` by subtracting the current node's value.

This solution efficiently checks all possible root-to-leaf paths and ensures that each node's value is appropriately considered in the sum.
