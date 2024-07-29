### Problem Statement
Given a binary tree and two distinct nodes, `p` and `q`, find their lowest common ancestor (LCA). The LCA of two nodes is defined as the deepest node that is an ancestor of both `p` and `q`.

### Function Definition
Here's the function signature for the problem in Python:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Implementation here
```

### Example Function Calls and Setup
1. **Tree Setup**: Create a binary tree and nodes `p` and `q`.
2. **Function Call**: Invoke the `tree_lca` function with the root of the tree and the two nodes `p` and `q`.

#### Example
```python
# Constructing the tree:
#       0
#      / \
#    -3   5
#    /   / \
#  -10  4   7
#         \
#          3

root = TreeNode(0)
root.left = TreeNode(-3)
root.left.left = TreeNode(-10)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(3)

# Nodes p and q
p = root.right.right        # Node with value 7
q = root.right.left.right   # Node with value 3

# Finding LCA
result = tree_lca(root, p, q)
print(result.val)  # Expected output should be the value of the LCA node
```

### High-Level Approach
1. **Recursive Traversal**: Use a recursive function to traverse the tree.
2. **Count Occurrences**: At each node, determine if it matches either `p` or `q` and count occurrences in left and right subtrees.
3. **Determine LCA**: The LCA is the node where the sum of matches in the subtree (including the current node) equals 2, indicating that both nodes `p` and `q` have been found in its subtree.
