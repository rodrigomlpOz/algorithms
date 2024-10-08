## Problem Statement

The problem requires us to determine if a given binary tree is a valid Binary Search Tree (BST). A valid BST is defined as follows:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

## Solution Approach

To solve this problem, a recursive approach can be used to check the validity of the BST. The function should ensure that:
- The value of each node falls within an allowable range defined by its position in the tree.
- The range for the left subtree nodes is `(-∞, root.val)`.
- The range for the right subtree nodes is `(root.val, ∞)`.

By maintaining these boundaries during the traversal, we can validate whether the BST property is maintained throughout the tree.


### Explanation

1. **Base Case**: If the `root` is `None`, it means the subtree is valid, so return `True`.
2. **Current Node Validation**: Check if the current node's value `val` lies within the allowed range `[lower, upper)`. If not, return `False`.
3. **Recursive Checks**:
   - For the left subtree, the new upper bound becomes the current node's value, and the lower bound remains unchanged.
   - For the right subtree, the new lower bound becomes the current node's value, and the upper bound remains unchanged.

### Example Usage

To test this function, you would typically create a binary tree using instances of `TreeNode` and then call `isValidBST()` on the root node. The function should return `True` if the tree is a valid BST and `False` otherwise.

```python
# Example usage:

# Creating a simple BST
#      2
#     / \
#    1   3

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

result = isValidBST(root)
print(result)  # Output: True

# Creating an invalid BST
#      5
#     / \
#    1   4
#       / \
#      3   6

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

result = isValidBST(root)
print(result)  # Output: False
```
