### Problem Statement:

Given a Binary Search Tree (BST), write a function to find the **k-th largest element** in the BST. The k-th largest element is defined as the element that would appear in the k-th position if all elements in the tree were sorted in descending order.

### Function Signature:

```python
from typing import Optional

class TreeNode:
    def __init__(self, data: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.data = data
        self.left = left
        self.right = right

def kth_largest(root: Optional[TreeNode], k: int) -> int:
    pass
```

### Example Usage:

```python
# Example BST:
#         19
#        /  \
#       7    43
#      /    /  \
#     3    23   47
#          /   /  \
#         21  37  53
#               \
#               41

# Tree structure creation
tree = TreeNode(19, 
                TreeNode(7, TreeNode(3)),
                TreeNode(43, 
                         TreeNode(23, TreeNode(21)), 
                         TreeNode(47, TreeNode(37, None, TreeNode(41)), TreeNode(53))))

# Find the 3rd largest element
result = kth_largest(tree, 3)  # Output: 43
print(result)
```

### High-Level Solution:

1. **Understanding the Problem**:
   - In a BST, the left subtree contains nodes smaller than the current node, and the right subtree contains nodes larger than the current node.
   - The largest elements are found in the right subtree, and the smallest elements are in the left subtree.
   - To efficiently find the k-th largest element, we can perform a **reverse in-order traversal** (right → root → left). This will allow us to visit the largest elements first.

2. **Reverse In-order Traversal**:
   - Start by traversing the right subtree to visit the largest elements.
   - Keep a count of how many nodes have been visited.
   - When the count reaches `k`, we have found the k-th largest element.
   - Stop further traversal once we find the k-th largest element to avoid unnecessary operations.

3. **Helper Function**:
   - The recursive helper function will traverse the tree in reverse in-order order, updating the count of visited nodes and returning the k-th largest element when found.

4. **Stopping Early**:
   - Once the k-th largest element is found, we can stop the traversal and return the result.

### Full Code:

```python
from typing import Optional

class TreeNode:
    def __init__(self, data: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.data = data
        self.left = left
        self.right = right

def kth_largest(root: Optional[TreeNode], k: int) -> int:
    # To track how many nodes we have visited
    count = 0
    result = None
    
    # Helper function for reverse in-order traversal
    def reverse_inorder(node: Optional[TreeNode]):
        nonlocal count, result
        if not node or result is not None:
            return
        
        # Visit right subtree first (largest elements)
        reverse_inorder(node.right)
        
        # Visit current node
        count += 1
        if count == k:
            result = node.data
            return
        
        # Visit left subtree (smaller elements)
        reverse_inorder(node.left)
    
    reverse_inorder(root)
    return result

# Example usage:

# Create the BST:
tree = TreeNode(19, 
                TreeNode(7, TreeNode(3)),
                TreeNode(43, 
                         TreeNode(23, TreeNode(21)), 
                         TreeNode(47, TreeNode(37, None, TreeNode(41)), TreeNode(53))))

# Find the 3rd largest element
result = kth_largest(tree, 3)  # Output: 43
print(result)
```

### Time and Space Complexity:

- **Time Complexity**: O(h + k), where `h` is the height of the tree. In the worst case (unbalanced tree), `h` could be `O(n)`. In a balanced tree, `h = O(log n)`. We may have to visit up to `k` nodes.
- **Space Complexity**: O(h), due to the recursion stack where `h` is the height of the tree.

### Summary:

- The solution uses a reverse in-order traversal to find the k-th largest element efficiently.
- By counting the number of nodes visited and stopping once the k-th largest is found, we avoid unnecessary traversal.
