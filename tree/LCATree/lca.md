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

def tree_lca(root, p, q):
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

In the simple recursive solution to the **Lowest Common Ancestor (LCA)** problem, we return `left` first when determining which subtree to continue with if one of the subtrees contains both `p` and `q`. This approach works because the logic is designed to explore both the left and right subtrees, and return a result based on where the nodes `p` and `q` are found.

Here’s a breakdown of why we return `left` first if it is non-null:

### Code:
```python
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None
    
    if root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right
```

### Key Points:

1. **If Both `p` and `q` Are Found in Different Subtrees:**
   - When both the left and right subtrees return non-null (i.e., `left` and `right` are both non-null), it means `p` is in one subtree and `q` is in the other. In this case, the current node (`root`) is the **lowest common ancestor**, so we return `root`.
   
2. **If Only One Subtree Contains `p` or `q`:**
   - If only one subtree returns non-null (either `left` or `right`), it means both `p` and `q` are located in the same subtree.
   - In this case, we **return the non-null value**, which means we return either `left` or `right`, whichever is non-null.
   
3. **Why `left` First:**
   - The reason we check `left` first is simply to follow the natural flow of traversal. When we recursively search the left and right subtrees, the search in the left subtree happens first.
   - If `left` contains one of the nodes (`p` or `q`), we don’t need to continue looking further in that subtree, and we return it immediately.
   - If the `left` subtree is `None` (i.e., `p` and `q` are not found there), we proceed to check `right`.

4. **Symmetry Between Left and Right**:
   - The choice to return `left` first is arbitrary. We could equally return `right` first. The core idea is that once we find a non-null subtree (whether it's the left or right subtree), we return it. Both sides are treated equally, and the same logic applies to either.

### How It Works:

- If **both `p` and `q`** are found in different subtrees, the current node is the LCA.
- If **both `p` and `q`** are found in the same subtree, the recursive call to that subtree will return the ancestor (or the node itself).
- If **neither `p` nor `q`** is found in the current subtree, the recursion will return `None`.

### Example Walkthrough:

#### Example Tree:
```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

Let’s find the LCA of `7` and `4`:

1. Start at `3`:
   - Recur on the left subtree (`5`).
   
2. At `5`:
   - Recur on the left subtree (`6`) → returns `None` (no `p` or `q` here).
   - Recur on the right subtree (`2`).
   
3. At `2`:
   - Recur on the left subtree (`7`) → returns `7` (found `p`).
   - Recur on the right subtree (`4`) → returns `4` (found `q`).
   
4. At `2`, both `left` and `right` are non-null, so return `2` (LCA of `7` and `4`).

5. At `5`, since the LCA was found in the right subtree, return `2`.

6. At `3`, return `2` as the final answer.

### Summary:

- We return `left` first simply because we search the **left subtree before the right subtree**. The decision to return `left` if it’s non-null is based on the order in which we traverse the tree.
- If `left` is `None`, we return `right`. If both `left` and `right` are non-null, it means we've found both `p` and `q` in different subtrees, and the current node is the LCA.
- This approach is symmetrical and would work just as well if we searched the right subtree first. It’s about finding the first non-null subtree and continuing from there.
