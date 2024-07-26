## Problem Statement

Given a preorder traversal of a Binary Search Tree (BST), construct the BST. The BST should be constructed in such a way that for every node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater than the node's value.

### Function Signature

```python
from typing import List, Optional

class BinaryTreeNode:
    def __init__(self, data: int, left: 'BinaryTreeNode' = None, right: 'BinaryTreeNode' = None, size: int = None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size

def bst_from_preorder(preorder_sequence: List[int]) -> Optional[BinaryTreeNode]:
    pass
```

### Function Calls and Example Usage

```python
# Example usage:

# Given a preorder sequence
preorder_sequence = [10, 5, 1, 7, 15, 12, 18]

# Construct the BST
root = bst_from_preorder(preorder_sequence)

# The BST structure:
#        10
#       /  \
#      5   15
#     / \  / \
#    1  7 12 18
```

### High-Level Approach

1. **Base Case**: If the preorder sequence is empty, return `None` since there's no tree to construct.

2. **Root Node**: The first element of the preorder sequence is the root of the BST.

3. **Splitting Preorder Sequence**: Identify the index where the right subtree starts by finding the first element greater than the root. This separates the preorder sequence into two parts:
   - Left subtree elements (all elements less than the root)
   - Right subtree elements (all elements greater than the root)

4. **Recursive Construction**: Recursively construct the left and right subtrees using the separated preorder sequences.


### Explanation

- **Initialization**: The `BinaryTreeNode` class represents each node in the BST, containing the data, left and right children, and an optional size attribute.
- **BST Construction**:
  - The first element of the `preorder_sequence` is used as the root of the BST.
  - The sequence is split into left and right parts using an index `i`, which is determined by finding the first element greater than the root's value.
  - Recursive calls build the left and right subtrees.

This method ensures that the constructed tree maintains the properties of a BST, with a time complexity of \( O(n) \), where \( n \) is the number of elements in the `preorder_sequence`.
