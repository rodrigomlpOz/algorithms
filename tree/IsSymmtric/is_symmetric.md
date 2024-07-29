## Problem Statement

Given a binary tree, determine if it is symmetric around its center. A binary tree is symmetric if the left and right subtrees are mirror images of each other.

### Function Signature

```python
def is_symmetric(root):
    pass
```

### Input Parameters

- `root`: The root node of the binary tree. Each node contains an integer value, a reference to the left child, and a reference to the right child.

### Output

- A boolean value indicating whether the tree is symmetric.

### Example

Consider the following binary tree:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

- **Input:** `root = TreeNode(1)`
  - `root.left = TreeNode(2)`
    - `root.left.left = TreeNode(3)`
    - `root.left.right = TreeNode(4)`
  - `root.right = TreeNode(2)`
    - `root.right.left = TreeNode(4)`
    - `root.right.right = TreeNode(3)`
- **Output:** `True`

The tree is symmetric as the left subtree is a mirror image of the right subtree.

### High-Level Approach

1. **Base Case**: If the tree is empty (`root` is `None`), it is symmetric by definition.

2. **Recursive Check for Symmetry**:
   - Use a helper function `symmetry(left_node, right_node)` that checks if two nodes are mirror images.
   - The function should return `True` if:
     - Both nodes are `None`.
     - The values of `left_node` and `right_node` are equal, and the left child of `left_node` is a mirror image of the right child of `right_node`, and vice versa.
   - The function should return `False` if:
     - One of the nodes is `None` and the other is not.
     - The values of the nodes are not equal.

3. **Recursive Traversal**: Start the recursive check from the root's left and right children. 

The implementation should focus on recursively verifying that the two subtrees are mirror images by comparing corresponding nodes and their children.
