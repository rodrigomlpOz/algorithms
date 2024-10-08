### Problem Statement:

Given a Binary Search Tree (BST), find the **lowest common ancestor (LCA)** of two given nodes in the BST. The lowest common ancestor is defined as the lowest node in the tree that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

Since it's a Binary Search Tree, the properties of BST can be used:
- All nodes in the left subtree are smaller than the current node.
- All nodes in the right subtree are larger than the current node.

### Function Signature:

```python
def lowestCommonAncestor(root, p, q):
    pass
```

### Example Usage:

```python
# Example BST:
#         6
#        / \
#       2   8
#      / \ / \
#     0  4 7  9
#       / \
#      3   5

# Tree structure creation
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)


p = root.left.right.left  # Node with value 3
q = root.left.right.right  # Node with value 5

result = lowestCommonAncestor(root, p, q)  # Output: 4
print(result.val)  # Should print 4
```

### High-Level Solution:

In a Binary Search Tree, the LCA of two nodes `p` and `q` can be determined by leveraging the properties of the BST. Here's the reasoning:

1. **BST Property**: 
   - If both `p` and `q` are smaller than the current node, then both nodes are in the left subtree, so we move to the left subtree.
   - If both `p` and `q` are larger than the current node, then both nodes are in the right subtree, so we move to the right subtree.
   - If one of `p` and `q` is on one side of the current node and the other is on the other side, the current node is the LCA.

2. **Recursion or Iteration**:
   - The function can be implemented either recursively or iteratively. We’ll explore both approaches below.

### Full Code Solution:

#### Iterative Solution:

```python
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Iterate through the BST
    while root:
        if p.val < root.val and q.val < root.val:
            # If both nodes are smaller than the root, move to the left subtree
            root = root.left
        elif p.val > root.val and q.val > root.val:
            # If both nodes are larger than the root, move to the right subtree
            root = root.right
        else:
            # We've found the split point, so this is the LCA
            return root
```

#### Recursive Solution:

```python
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Base case: if we reach a leaf node, or we find the LCA
    if not root:
        return None
    
    # If both nodes are smaller than the current root, search in the left subtree
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    
    # If both nodes are larger than the current root, search in the right subtree
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    
    # Otherwise, we have found the split point, so root is the LCA
    return root
```

### Explanation:

1. **Start at the root**: Begin at the root of the tree.
2. **Check the values**: 
   - If both `p` and `q` are less than the root's value, both nodes must be in the left subtree, so we move left.
   - If both `p` and `q` are greater than the root's value, both nodes must be in the right subtree, so we move right.
   - If one is smaller and the other is greater, the current node is the **lowest common ancestor**.
3. **Return the result**: The first time we encounter a node that satisfies the LCA condition, we return it.

### Time and Space Complexity:

- **Time Complexity**: O(h), where `h` is the height of the BST. In the worst case, this is O(n) for a completely unbalanced tree. In a balanced tree, the height is O(log n).
- **Space Complexity**: 
   - **Iterative**: O(1), since we're using a constant amount of space.
   - **Recursive**: O(h) due to the recursion stack.

### Example Usage Continued:

```python
# Example usage 2: LCA of nodes 2 and 4
p = root.left         # Node with value 2
q = root.left.right   # Node with value 4

result = lowestCommonAncestor(root, p, q)  # Output: 2
print(result.val)  # Should print 2
```

In this example:
- The LCA of nodes `2` and `4` is `2`, as `2` is the ancestor of `4` and itself. Therefore, `2` is the lowest common ancestor.
