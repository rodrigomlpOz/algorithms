## Problem Statement

Given a binary tree where each node contains a `data` attribute and a `size` attribute (the number of nodes in the subtree rooted at that node), write a function to find the k-th node in an in-order traversal of the tree. The in-order traversal visits nodes in the following order: left subtree, current node, and then right subtree.

## Function Signature

```python
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size

def find_kth_node_binary_tree(tree, k):
    pass
```

### Input Parameters

- `tree`: The root node of the binary tree, represented by the `BinaryTreeNode` class.
- `k`: An integer representing the position of the node to find in the in-order traversal.

### Example Inputs and Outputs

**Example 1:**

- **Input:**
  - `tree` with structure:
    ```
       3
      / \
     1   4
      \
       2
    ```
  - `k = 1`

- **Output:** The node with `data = 1`

**Example 2:**

- **Input:**
  - `tree` with structure:
    ```
         5
        / \
       3   7
      / \   \
     2   4   8
    / 
   1
    ```
  - `k = 4`

- **Output:** The node with `data = 4`

### High-Level Approach

1. **Utilize the `size` Attribute**: Use the `size` attribute of each node to determine the position of nodes in the in-order traversal efficiently.
   
2. **In-Order Traversal Logic**:
    - **Left Subtree Size**: If the size of the left subtree is greater than or equal to `k`, the k-th node lies in the left subtree.
    - **Current Node**: If the left subtree size plus one equals `k`, the current node is the k-th node.
    - **Right Subtree**: If the left subtree size plus one is less than `k`, the k-th node lies in the right subtree. Adjust `k` to account for the nodes in the left subtree and the current node.

3. **Iterative Approach**: Implement an iterative solution that traverses the tree while maintaining the count of nodes visited, leveraging the `size` attribute to quickly locate the k-th node.

### Function Calls with Setup

```python
# Example function call
root = BinaryTreeNode(3)
root.left = BinaryTreeNode(1)
root.right = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(2)

# Assuming the size attribute has been correctly populated
root.size = 4
root.left.size = 2
root.right.size = 1
root.left.right.size = 1

k = 1
kth_node = find_kth_node_binary_tree(root, k)
print(kth_node.data)  # Output: 1
```

In this setup, the `find_kth_node_binary_tree` function is expected to find the 1st node in the in-order traversal of the given binary tree, which should return the node with `data = 1`.
