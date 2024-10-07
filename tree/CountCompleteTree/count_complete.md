### Problem Statement:
Given the root of a **complete binary tree**, return the number of the nodes in the tree.

A **complete binary tree** is a binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.

The challenge is to implement this function efficiently by taking advantage of the properties of a complete binary tree, rather than simply counting all nodes one by one.

### Function Signature:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: TreeNode) -> int:
    pass
```

### Function Calls:
```python
# Example 1:
# Input tree:
#        1
#       / \
#      2   3
#     / \ / 
#    4  5 6  

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(countNodes(root))  # Output: 6

# Example 2:
# Input tree: Only the root
root2 = TreeNode(1)

print(countNodes(root2))  # Output: 1

# Example 3:
# Input tree: Empty tree
root3 = None

print(countNodes(root3))  # Output: 0
```

### High-Level Solution:

1. **Base Case (Empty Tree):**
   - If the tree is empty (i.e., the root is `None`), return `0`.

2. **Calculate the Depth:**
   - Compute the depth of the tree by traversing down the leftmost path. The depth is the number of edges from the root to the deepest node.
   
3. **Check Depths of Left and Right Subtrees:**
   - Compare the depth of the left and right subtrees:
     - If the left and right subtree depths are the same, it means the left subtree is a **perfect binary tree**, and we can calculate its number of nodes using the formula \(2^{\text{depth}} - 1\) plus `1` for the root, and then recursively count the nodes in the right subtree.
     - If the left subtree has a greater depth than the right, the right subtree is a **perfect binary tree** (one level smaller), and we calculate its number of nodes similarly and recursively count the nodes in the left subtree.

4. **Recursion:**
   - Use recursion to solve the subtrees efficiently, reducing the overall complexity to O(log(n)²), where `n` is the number of nodes.

### Time Complexity:
- O(log(n)²): We calculate the depth O(log(n)) times, and each depth calculation takes O(log(n)) steps.

### Pseudocode Explanation:
1. **Helper Function (`get_depth`):**
   - This function calculates the depth of a tree by following the leftmost path.
   
2. **Main Logic (`countNodes`):**
   - If the tree is empty, return `0`.
   - Calculate the left and right subtree depths.
   - If the depths are the same, the left subtree is perfect. Use the formula to calculate its nodes and recursively call `countNodes` on the right subtree.
   - If the depths differ, the right subtree is perfect. Calculate its nodes and recursively call `countNodes` on the left subtree.