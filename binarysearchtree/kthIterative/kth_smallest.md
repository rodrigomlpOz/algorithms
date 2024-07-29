## Problem Statement

Given a Binary Search Tree (BST), write a function to find the kth smallest element in the tree. The tree is structured such that each node contains a value, and there is a left and right child. The left child nodes contain values less than the parent node, and the right child nodes contain values greater than the parent node.

## Function Signature

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def kth_smallest_bst(root, k):
    pass
```

### Input Parameters

- `root`: The root node of the BST, represented by the `TreeNode` class.
- `k`: An integer representing the position of the smallest element to find in the BST.

### Example Inputs and Outputs

**Example 1:**

Input: `root = [3,1,4,null,2]`, `k = 1`
```
   3
  / \
 1   4
  \
   2
```
Output: `1`

**Example 2:**

Input: `root = [5,3,6,2,4,null,null,1]`, `k = 3`
```
       5
      / \
     3   6
    / \
   2   4
  /
 1
```
Output: `3`

### High-Level Approach

1. **In-Order Traversal**: Utilize the in-order traversal of the BST, which visits nodes in ascending order. This property is useful for finding the kth smallest element.
  
2. **Iterative Approach Using Stack**: 
    - Use a stack to manage the nodes during traversal. 
    - Start from the root and traverse to the leftmost node, pushing each node onto the stack.
    - Pop nodes from the stack and decrement `k` each time a node is popped. When `k` reaches 0, the current node is the kth smallest element.
  
3. **Edge Cases**: Consider cases where the tree is empty or `k` is larger than the number of nodes in the tree. Handle such cases by returning `None` or raising an appropriate error.

### Function Calls with Setup

```python
# Building the BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

# Example function call
k = 3
print(kth_smallest_bst(root, k))  # Output: 3
```

In this setup, the function `kth_smallest_bst` is expected to find the 3rd smallest element in the given BST, which should return `3`.
