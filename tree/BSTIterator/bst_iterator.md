### Problem Statement:
You are tasked with implementing a class `BSTIterator` that represents an iterator for in-order traversal of a Binary Search Tree (BST). The iterator will allow sequential access to the BST nodes, starting with the smallest element and moving to the largest.

The class must support the following operations:
1. **BSTIterator(TreeNode root)**: Initializes the iterator with the root node of a BST.
2. **boolean hasNext()**: Returns `true` if there is a next element in the in-order traversal, `false` otherwise.
3. **int next()**: Returns the next smallest number in the in-order traversal.

### Function Signature:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        pass
    
    def next(self) -> int:
        pass
    
    def hasNext(self) -> bool:
        pass
```

### Function Calls:
- **BSTIterator(TreeNode root)**: Called once with the root of the BST.
- **next()**: Called multiple times to retrieve the next smallest number in the BST.
- **hasNext()**: Called to check if there are more elements in the in-order traversal.

### High-Level Solution:

1. **Initialization (BSTIterator)**:
   - Use a stack to simulate the recursive behavior of in-order traversal.
   - Start by pushing all nodes along the leftmost path from the root onto the stack.
   - This ensures that the smallest element (leftmost) is on the top of the stack.

2. **next()**:
   - The top node of the stack is the next smallest element in the BST.
   - Pop this node from the stack and return its value.
   - If the popped node has a right child, push all nodes along the leftmost path of the right child onto the stack. This ensures that the next smallest element is always on top.

3. **hasNext()**:
   - Simply check if the stack is non-empty. If it is, there are more elements to return in the in-order traversal.

### Example Calls:
```python
# Example of constructing a tree and using BSTIterator:
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

# Initialize iterator
iterator = BSTIterator(root)

# Function calls
iterator.next()    # Returns 3
iterator.next()    # Returns 7
iterator.hasNext() # Returns True
iterator.next()    # Returns 9
iterator.hasNext() # Returns True
iterator.next()    # Returns 15
iterator.hasNext() # Returns True
iterator.next()    # Returns 20
iterator.hasNext() # Returns False
```

### Time and Space Complexity:
- **Time complexity**: Both `next()` and `hasNext()` are O(1) on average. While pushing nodes onto the stack may take O(h) where h is the height of the tree, each node is visited once.
- **Space complexity**: O(h), where h is the height of the tree, for storing the nodes in the stack during traversal.