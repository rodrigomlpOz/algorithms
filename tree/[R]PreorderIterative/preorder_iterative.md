## Problem Statement

Given a binary tree, implement an iterative method for performing a preorder traversal. Preorder traversal visits nodes in the following order: root, left subtree, right subtree. The tree is represented by `TreeNode` objects, where each node contains an integer value, a reference to the left child, and a reference to the right child.

### Function Signature

```python
def preorder_iterative(root):
    pass
```

### Input Parameters

- `root`: The root node of the binary tree.

### Output

- A list of integers representing the values of the nodes visited in preorder.

### Example

Given the following binary tree:

```
      0
     / \
   -3   9
   /   /
 -10  5
```

- **Input:** `root = TreeNode(0)`
  - `root.left = TreeNode(-3)`
    - `root.left.left = TreeNode(-10)`
  - `root.right = TreeNode(9)`
    - `root.right.left = TreeNode(5)`
- **Output:** `[0, -3, -10, 9, 5]`

### High-Level Approach

1. **Initialization**:
   - Create a stack to keep track of the nodes to be visited.
   - Initialize an empty list `ans` to store the values of nodes as they are visited.

2. **Preorder Traversal**:
   - Start with the root node. Push it onto the stack and process it by adding its value to the result list.
   - Continue to push left children onto the stack until reaching the end of the leftmost branch.
   - Once a node has no left child, pop from the stack and process the right child, if any.
   - Repeat the process until all nodes have been visited.

3. **Return Result**:
   - The list `ans` will contain the values of nodes in the order they were visited during the preorder traversal.

This approach ensures that each node is processed once, and the preorder traversal is conducted without using recursion, which can be beneficial for managing larger trees or avoiding stack overflow issues in languages with limited stack sizes.
