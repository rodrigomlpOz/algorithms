## Problem Statement

The problem "Merge Two Binary Trees" involves merging two binary trees into a new binary tree. The merge rule is that if two nodes overlap, their values are added, and the result is stored in the new tree. Otherwise, the non-null node will be used as the node of the new tree.

### Function Signature

```python
def mergeTrees(t1, t2):
    pass
```

### Input Parameters

- `t1`: The root node of the first binary tree.
- `t2`: The root node of the second binary tree.

### Output

- The root node of the new merged binary tree.

### Example

Consider the following binary trees:

**Tree 1:**

```
    1
   / \
  3   2
 / 
5  
```

**Tree 2:**

```
    2
   / \
  1   3
   \   \
    4   7
```

**Merged Tree:**

```
    3
   / \
  4   5
 / \   \
5   4   7
```

### High-Level Approach

1. **Base Cases**:
   - If both nodes are `None`, return `None`.
   - If one of the nodes is `None`, return the other node because there is nothing to merge at that position.

2. **Recursive Merging**:
   - If both nodes are present, create a new node with the sum of the values from `t1` and `t2`.
   - Recursively merge the left children of `t1` and `t2`, and assign the result to the left child of the new node.
   - Recursively merge the right children of `t1` and `t2`, and assign the result to the right child of the new node.

3. **Return Result**: The function returns the root of the new merged binary tree.
