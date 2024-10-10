### Function Signature:
```python
def min_absolute_difference_bst(root):
    pass
```

### High-Level Solution:
1. **In-order Traversal**: Since the Binary Search Tree (BST) is sorted in an in-order traversal (left subtree -> node -> right subtree), the minimum absolute difference will be between two consecutive nodes during this traversal.
2. **Tracking Previous Node**: Keep track of the previous node visited during the traversal to calculate the difference with the current node.
3. **Updating Minimum Difference**: As we traverse, continuously update the minimum difference found so far.
4. **Edge Case**: If the tree has fewer than two nodes, there is no valid pair to compare, and the function should handle this gracefully.

### TreeNode Definition:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Function Calls with Print Statements:

```python
# Example 1: A simple BST
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

print(min_absolute_difference_bst(root1))  # Expected output: 1 (difference between 2 and 3)

# Example 2: Another BST with larger values
root2 = TreeNode(1)
root2.right = TreeNode(5)
root2.right.left = TreeNode(3)

print(min_absolute_difference_bst(root2))  # Expected output: 2 (difference between 3 and 5)

# Example 3: Edge case with only one node
root3 = TreeNode(10)

print(min_absolute_difference_bst(root3))  # Expected output: None (since no valid pair exists)
```