## Problem Statement

The problem involves inverting a binary tree. Inverting a binary tree means swapping the left and right children of all nodes in the tree. The problem is commonly visualized as flipping the tree horizontally.

### Function Signature

```python
def invert_tree(root):
    pass
```

### Input Parameters

- `root`: The root node of the binary tree. Each node is represented by an instance of `TreeNode`, containing the attributes `val` (the value of the node), `left` (the left child), and `right` (the right child).

### Output

- The function should return the root of the inverted binary tree.

### Example

Consider the following binary tree before and after inversion:

**Before Inversion:**

```
    1
   / \
  2   3
 / \ / \
4  5 6  7
```

**After Inversion:**

```
    1
   / \
  3   2
 / \ / \
7  6 5  4
```

### High-Level Approach

1. **Level-Order Traversal (BFS)**: Use a queue to perform a level-order traversal of the tree. This ensures that nodes are visited level by level, which is suitable for swapping the children of each node.

2. **Swapping Children**: For each node visited, swap its left and right children.

3. **Queue Operations**: Enqueue the left and right children of the current node after they have been swapped. This step ensures that all nodes are eventually visited and their children swapped.

4. **Return the Root**: Once all nodes have been processed and the tree has been inverted, return the root of the tree.

This approach ensures that the tree is inverted in a breadth-first manner, which can be advantageous for handling large trees in memory, as it processes one level at a time.
