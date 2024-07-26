## Problem Statement

Given an array where elements are sorted in ascending order, convert it to a height-balanced binary search tree (BST). A height-balanced BST is a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

### Function Signature

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    pass
```

### High-Level Approach

1. **Divide and Conquer**: The middle element of the array will be the root of the BST. The elements to the left of the middle element will form the left subtree, and the elements to the right will form the right subtree.
2. **Recursion**: Recursively apply this approach to the left and right subarrays to construct the left and right subtrees.


### Explanation

1. **Helper Function**: The `helper` function takes the indices of the current subarray (`left` and `right`). It returns `None` if the subarray is invalid (i.e., `left > right`).
2. **Middle Element**: The middle element of the subarray is chosen as the root of the subtree. This ensures that the tree remains height-balanced.
3. **Recursion**:
   - The left subtree is constructed from the left half of the subarray (`left` to `mid - 1`).
   - The right subtree is constructed from the right half of the subarray (`mid + 1` to `right`).

### Example Usage

To test this function, you can call `sortedArrayToBST()` with a sorted array and print the resulting tree.

```python
# Example usage:

def print_inorder(node: Optional[TreeNode]):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=' ')
    print_inorder(node.right)

# Sorted array
nums = [-10, -3, 0, 5, 9]

# Convert to height-balanced BST
root = sortedArrayToBST(nums)

# Print the tree in inorder to verify
print_inorder(root)
# Expected output: -10 -3 0 5 9
```

### Explanation of Example

- **Input Array**: `[-10, -3, 0, 5, 9]`
- **Output**: A height-balanced BST that would look like:
  ```
         0
       /   \
     -10    5
       \    / 
       -3  9
  ```
- **Inorder Traversal**: The inorder traversal of the resulting BST should match the original sorted array.
