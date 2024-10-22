The "tree diameter" problem involves finding the longest path between two nodes in a tree. The longest path in a tree is called its diameter. The path doesn't necessarily pass through the root, and it can be found anywhere in the tree. This is a common problem in tree data structures.

### Problem Statement:
Given a tree represented by its nodes and edges, write a function to find the diameter (the length of the longest path between two nodes) of the tree.

### Function Definition:
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_diameter(root: TreeNode) -> int:
    # Your code here
    pass
```

### Function Calls Example:

```python
# Example tree
#       1
#      / \
#     2   3
#    / \
#   4   5

node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, left=node4, right=node5)
node3 = TreeNode(3)
root = TreeNode(1, left=node2, right=node3)

# Call the function
print(tree_diameter(root))  # Expected output: 3 (the longest path is 4 -> 2 -> 1 -> 3)
```

### High-Level Solution:
1. **Diameter Definition**: The diameter is the longest path between any two nodes in the tree. This path could involve passing through the root or any other node.

2. **Recursive Strategy**: 
   - For each node, compute two things:
     1. The height of its left and right subtrees.
     2. The diameter that passes through the node (i.e., the sum of the heights of the left and right subtrees).
   
   - The diameter at any given node is either:
     - The sum of the heights of its left and right subtrees (if the path passes through the node).
     - The maximum diameter of the left or right subtree (if the longest path doesn't pass through the node).
   
3. **Global Diameter**: Use a variable to track the maximum diameter found during the recursive traversal.

4. **Time Complexity**: Since each node is visited once, the time complexity is \(O(N)\), where \(N\) is the number of nodes.
