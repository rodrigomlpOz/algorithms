## Problem Statement: Create a List of Leaves of a Binary Tree

Given a binary tree, write a function to create a list of its leaf nodes. A leaf node is a node that does not have any children.

### Function Signature

```python
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def create_list_of_leaves(tree):
    pass
```

### Example Usage

1. **Example 1:**
   - **Input:**
     - Binary Tree:
       ```
           1
          / \
         2   3
        /|   |\
       4 5   6 7
       ```
   - **Output:** [4, 5, 6, 7]

2. **Example 2:**
   - **Input:**
     - Binary Tree:
       ```
           1
          / \
         2   3
          \
           4
            \
             5
       ```
   - **Output:** [5, 3]

### High-Level Approach

1. **Base Case**: If the tree is empty (the node is `None`), return an empty list.
2. **Leaf Node Case**: If the node is a leaf (no left and right children), return a list containing this node.
3. **Recursive Case**: If the node is not a leaf, recursively find the leaves of the left and right subtrees and concatenate the results.

### Explanation

1. **Base Case**: If the input `tree` is `None`, the function returns an empty list. This handles the scenario where the tree is empty.
2. **Leaf Node Case**: If the current node has no left or right children, it is a leaf node. The function returns a list containing just this node.
3. **Recursive Case**: If the current node is not a leaf, the function recursively calls itself to process the left and right subtrees. The results from these recursive calls are concatenated to form the final list of leaves.

### Example Usage

```python
# Example usage:

# Constructing the tree:
#        1
#       / \
#      2   3
#     /|   |\
#    4 5   6 7

node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node2 = TreeNode(2, left=node4, right=node5)
node3 = TreeNode(3, left=node6, right=node7)
root = TreeNode(1, left=node2, right=node3)

# Finding the leaves
leaves = create_list_of_leaves(root)
# Printing the values of the leaves
for leaf in leaves:
    print(leaf.val)  # Output: 4 5 6 7
```

In this example, the function correctly identifies the leaf nodes (4, 5, 6, 7) and returns them in a list. The example demonstrates the function's capability to process a binary tree and extract its leaves efficiently.
