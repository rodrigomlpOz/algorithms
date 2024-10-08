## Problem Statement

Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

### Function Signature

```python
def levelOrder(root):
    pass

# Creating nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

# Building the tree
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

levelOrder = levelOrder(root)
```

### Input Parameters

- `root`: The root node of the binary tree. Each node is represented by an instance of `TreeNode`, containing the attributes `val` (the value of the node), `left` (the left child), and `right` (the right child).

### Output

- A list of lists, where each inner list contains the values of the nodes at that level of the binary tree.

### Example

Consider the following binary tree:

```
    1
   / \
  2   3
 / \ / \
4  5 6  7
```

- **Input:** `root = TreeNode(1)`
  - `root.left = TreeNode(2)`
    - `root.left.left = TreeNode(4)`
    - `root.left.right = TreeNode(5)`
  - `root.right = TreeNode(3)`
    - `root.right.left = TreeNode(6)`
    - `root.right.right = TreeNode(7)`
- **Output:** `[[1], [2, 3], [4, 5, 6, 7]]`

### High-Level Approach

1. **Initialize a Queue**: Use a queue to help with the level-order traversal. Start by adding the root node to the queue.

2. **Level Order Traversal**:
   - While there are nodes in the queue, process each level of the tree.
   - For each level, initialize an empty list `level` to hold the node values for that level.
   - Record the number of nodes at the current level (`size`) by checking the length of the queue.
   - For each node at the current level, dequeue the node, record its value, and enqueue its left and right children (if they exist).

3. **Collect Results**: After processing all nodes at a level, add the `level` list to the result list `ans`.

4. **Return Results**: After processing all levels, return `ans`.

This approach ensures that each level of the tree is processed separately and that the node values are collected in the correct order. The use of a queue ensures that nodes are processed in the order they appear at each level, which is crucial for level-order traversal.
