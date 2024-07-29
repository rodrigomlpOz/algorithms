## Problem Statement

The problem involves finding the in-order successor of a given node in a binary tree. The in-order successor of a node is the next node in the in-order traversal of the binary tree. In other words, it is the smallest node in the tree that is larger than the given node. Each node has a `parent` pointer in addition to the left and right child pointers.

### Function Signature

```python
def find_successor(node):
    pass
```

### Input Parameters

- `node`: A reference to a node in a binary tree, where each node has attributes `val` (the value of the node), `left` (the left child), `right` (the right child), and `parent` (the parent node).

### Output

- The function should return the in-order successor of the given node. If the given node is the rightmost node in the tree, the function should return `None`.

### Example

Consider the following binary tree:

```
        20
       /  \
     10    30
     / \   /
    5  15 25
       \
       17
```

- **Input:** A reference to the node with value `15`.
- **Output:** The node with value `17`, as it is the in-order successor of `15`.

### High-Level Approach

1. **Case 1: Node has a Right Subtree**
   - If the node has a right child, the successor is the leftmost node in the right subtree. This is because, in an in-order traversal, the leftmost node in the right subtree is the first node that comes after the given node.

2. **Case 2: Node does not have a Right Subtree**
   - If the node does not have a right child, the successor is one of its ancestors. Specifically, it is the lowest ancestor of the node whose left subtree contains the node. This can be found by traversing up the tree using the `parent` pointer until a node is found that is the left child of its parent.

3. **Return Result**
   - If no such ancestor exists (i.e., the node is the rightmost node in the tree), the function should return `None`.

This approach ensures that the successor is found efficiently by either navigating down to the right subtree or by moving up to the nearest ancestor.
