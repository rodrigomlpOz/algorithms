## Problem Statement

Given a Binary Search Tree (BST) and a value \( k \), write a function to find the first node in the BST whose value is greater than \( k \). If such a node does not exist, the function should return -1.

### Function Signature

```python
from typing import Optional

class TreeNode:
    def __init__(self, data: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.data = data
        self.left = left
        self.right = right

def find_first_greater_than_k(tree: Optional[TreeNode], k: int) -> Optional[TreeNode]:
    pass

def find_first_greater_than_k_wrapper(tree: Optional[TreeNode], k: int) -> int:
    pass
```

### Function Calls and Example Usage

```python
# Example usage:

# Create a sample BST
#         19
#        /  \
#       7    43
#      /    /  \
#     3    23   47
#          /   /  \
#         21  37  53
#               \
#               41

# Tree structure creation
tree = TreeNode(19, 
                TreeNode(7, TreeNode(3)),
                TreeNode(43, 
                         TreeNode(23, TreeNode(21)), 
                         TreeNode(47, TreeNode(37, None, TreeNode(41)), TreeNode(53))))

# Find the first node with value greater than 23
result = find_first_greater_than_k_wrapper(tree, 23)  # Output: 43
print(result)
```

### High-Level Approach

1. **Traversal**: Start from the root and traverse the tree.
2. **Comparison**: For each node:
   - If the node's value is greater than \( k \), move to the left child to find a potentially smaller value that is still greater than \( k \).
   - If the node's value is less than or equal to \( k \), move to the right child since all values in the left subtree (including the current node) are not greater than \( k \).
3. **Tracking the Result**: Maintain a variable to track the first node encountered with a value greater than \( k \).

