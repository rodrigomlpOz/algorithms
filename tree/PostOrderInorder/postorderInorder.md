### Problem Definition:
Given two integer arrays `inorder` and `postorder`, where:
- `inorder` is the inorder traversal of a binary tree.
- `postorder` is the postorder traversal of the same binary tree.

Construct and return the binary tree from these traversals.

### Function Definition:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree_from_inorder_postorder(inorder, postorder):
    pass
```

### Example Function Calls:

**Example 1:**
```python
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

root = construct_binary_tree_from_inorder_postorder(inorder, postorder)
```
Expected Output Tree:
```
        3
       / \
      9   20
         /  \
        15   7
```

**Example 2:**
```python
inorder = [-1]
postorder = [-1]

root = construct_binary_tree_from_inorder_postorder(inorder, postorder)
```
Expected Output Tree:
```
  -1
```

### High-Level Solution:

1. **Tree Structure:**
   - In the **postorder traversal**, the last element is always the **root** of the tree.
   - In the **inorder traversal**, elements to the left of the root are part of the **left subtree**, and elements to the right of the root are part of the **right subtree**.

2. **Recursion:**
   - Find the root of the tree by taking the last element from `postorder`.
   - Use the `inorder` array to determine which nodes are in the left and right subtrees by finding the position of the root in the `inorder` list.
   - Recursively build the left and right subtrees by slicing the `inorder` and `postorder` arrays accordingly.

3. **Base Case:**
   - When the `inorder` or `postorder` array is empty, return `None`.

### Step-by-Step:
1. The last element of `postorder` is the root.
2. Find this root in the `inorder` array.
3. Elements left of the root in `inorder` form the left subtree; elements right of the root form the right subtree.
4. Recursively construct left and right subtrees using updated slices of `inorder` and `postorder`.
5. Return the constructed root.

This approach ensures the tree is constructed in O(n) time where n is the number of nodes, as each element is visited once during the traversal.