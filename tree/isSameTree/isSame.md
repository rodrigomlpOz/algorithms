### Problem Statement:

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same values at each corresponding position.

### Function Signature:
```python
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    pass
```

### Function Calls with Print:
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example trees that are the same
# Tree p:      1               Tree q:      1
#            /   \                        /   \
#           2     3                      2     3

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# Check if p and q are the same tree
print(isSameTree(p, q))  # Expected output: True

# Example trees that are different
# Tree p:      1               Tree q:      1
#            /                            /   \
#           2                            2     3

p2 = TreeNode(1)
p2.left = TreeNode(2)

q2 = TreeNode(1)
q2.left = TreeNode(2)
q2.right = TreeNode(3)

# Check if p2 and q2 are the same tree
print(isSameTree(p2, q2))  # Expected output: False
```

### High-Level Solution:

1. **Base Case:**
   - If both `p` and `q` are `None`, they are considered the same tree (both are empty).
   - If one of `p` or `q` is `None` while the other is not, they are different trees.
   
2. **Recursive Step:**
   - If the values of `p` and `q` are different, return `False`.
   - Recursively check the left subtrees and right subtrees of both `p` and `q`.
   - Return `True` if the values are the same and both subtrees are identical.

This recursive approach ensures that we traverse both trees simultaneously, checking both the structure and values at each node.