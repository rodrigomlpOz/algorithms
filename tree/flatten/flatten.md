## Problem: Flatten Binary Tree to Linked List

The problem involves converting a given binary tree into a flattened linked list in place. The flattened tree should follow the same order as a pre-order traversal of the binary tree, meaning that the left child pointer should be set to `None` for all nodes, and the right child pointer should point to the next node in the order.

### Function Signature

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: Optional[TreeNode]) -> None:
    # Function to modify the binary tree in-place
    pass
```

### Approach

The idea is to flatten the binary tree into a linked list using a depth-first search approach. The steps involve:
1. **Recursion and Base Case:** If the current node is `None`, return `None`. If it's a leaf node (no children), return the node itself as it doesn't need further modification.
2. **Recursive Flattening:** Recursively flatten the left and right subtrees.
3. **Reconfiguration:** If the node has a left subtree:
   - Attach the flattened left subtree to the right of the current node.
   - Find the tail of the flattened left subtree and attach the flattened right subtree to the end of this tail.
   - Set the left child of the current node to `None` to maintain the "linked list" structure.

The function `flattenTree` returns the rightmost node (tail) of the subtree after flattening, which helps in connecting the subtrees correctly.


### Explanation

- **TreeNode Class:** Represents each node in the binary tree with `val` for value, `left` for the left child, and `right` for the right child.
- **flattenTree Function:** This helper function performs the recursive flattening. It handles the `None` and leaf node scenarios and recursively flattens the left and right subtrees. The function modifies the node's right child pointer to ensure the left subtree, once flattened, appears before the right subtree. It also ensures the left child pointer is set to `None`.
- **flatten Function:** This is the main function that initiates the flattening process starting from the root of the tree.

The tree is modified in place, meaning the original tree structure is altered to form a single right-skewed tree (which represents a linked list). The resulting "linked list" follows the order of nodes as they appear in a pre-order traversal of the original tree.
