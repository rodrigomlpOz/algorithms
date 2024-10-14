### Problem Statement
Given the root of a binary tree, return the values of the nodes that are visible from the right side. The right side view of a tree contains the last node of each level when the tree is traversed from top to bottom.

### Function Signature
```python
def rightSideView(root):
    pass
```

Where:
- `root` is the root node of the binary tree.
- The function should return a list of integers representing the node values visible from the right side of the tree.

### Function Calls
Example 1:
```python
# Input tree: [1, 2, 3, null, 5, null, 4]
#        1
#      /   \
#     2     3
#      \      \
#       5      4

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # The value of the node
        self.left = left      # Left child node
        self.right = right    # Right child node


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(rightSideView(root))  # Output: [1, 3, 4]
```

Example 2:
```python
# Input tree: [1, 2, 3, 4]
#        1
#      /   \
#     2     3
#    /
#   4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(rightSideView(root))  # Output: [1, 3, 4]
```

### High-Level Solution Definition
1. **Level Order Traversal**: Perform a level-order (BFS) traversal of the tree, but instead of recording all nodes at each level, only capture the last node at each level.
   
2. **Queue for Traversal**: Use a queue to traverse the tree level by level. For each level, enqueue the child nodes (first the left child, then the right child) of the current node.

3. **Capture the Last Node**: As you process each level, keep track of the last node seen (the rightmost node). Once you've processed all nodes at that level, add the last node's value to the result list.

### Algorithm Steps:
1. If the tree is empty, return an empty list.
2. Initialize a queue with the root node and an empty list for the result.
3. While there are nodes in the queue:
   - Get the number of nodes at the current level.
   - For each node at the level, process the nodes from left to right, and keep track of the last node's value.
   - At the end of the level, add the last node's value to the result list.
4. Return the result list containing the rightmost node values.

