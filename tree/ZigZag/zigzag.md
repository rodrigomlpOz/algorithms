### Problem Statement
Given a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

### Function Definition
Here's the function signature for the problem in Python:

```python
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def zigzagLevelOrder(root: TreeNode):
    pass
```

### High-Level Approach
1. **Breadth-First Search (BFS) with Zigzag Order**: Use a queue to traverse the tree level by level, while keeping track of the current traversal order (left-to-right or right-to-left).
2. **Alternate Order**: Use a flag to alternate between appending values in normal order and reversed order for each level.
3. **Collect Results**: Collect the values of nodes level-by-level and add them to the result list in the appropriate order based on the current traversal direction.

### Example Function Call and Setup
To use the `zigzagLevelOrder` function, first create the binary tree and then call the function with the root of the tree.

#### Example
```python
# Constructing the tree:
#       3
#      / \
#     9  20
#       /  \
#      15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Zigzag level order traversal
sol = Solution()
result = sol.zigzagLevelOrder(root)
print(result)  # Expected output: [[3], [20, 9], [15, 7]]
```

This code performs a zigzag level order traversal of the binary tree, collecting and returning the values level by level in the specified order.
