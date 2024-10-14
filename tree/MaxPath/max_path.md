
### Key Concepts:

1. **Binary Tree**: Each node in the tree has a value and possibly two children (left and right).
2. **Path**: A path in the tree is a sequence of nodes connected by edges. The path sum is the sum of the values of all nodes along the path.
3. **Max Path Sum**: We are tasked with finding the path with the largest sum. The path can go through any number of nodes and does not have to start at the root or end at a leaf. It can start and end at any node in the tree.

### Intuition Behind the Algorithm:

For each node in the tree, there are two important things we care about:
- **Maximum gain from this node to its parent**: This is the best possible path sum we can achieve by starting from this node and continuing either to its left or right child, but not both. We need this to "pass on" the maximum sum to its parent, so the parent can compute its own max path.
- **Maximum path sum that passes through this node**: This considers the node itself, the left child, and the right child. The path starts from the left child, goes through the node, and ends at the right child.

For each node:
- We calculate the maximum gain from the left and right children.
- We then compute the maximum path sum that includes both children and the node itself.
- We update the global maximum path sum if the current node provides a better path sum than we’ve seen before.
- Finally, we return the maximum gain that the current node can contribute to its parent, which will be the node's value plus the larger of the left or right gain.

### Steps in the Algorithm:

1. **Recursive Function**:
   We use a recursive function `max_gain(node)` to calculate the maximum gain starting from each node and updating the global maximum path sum.
   
2. **Base Case**:
   If the node is `None`, return `0`. This means that an empty node doesn't contribute to the path sum.

3. **Calculate Left and Right Gains**:
   Recursively compute the maximum gain starting from the left child and the right child of the current node. If the gain from any child is negative, we treat it as `0`, meaning we don't include that child in the path.

4. **New Path Sum**:
   At each node, calculate the path sum that includes the node itself, the left gain, and the right gain. This is the path that "passes through" the current node.

5. **Update the Global Maximum Sum**:
   Compare the current path sum (left gain + right gain + node’s value) with the global maximum sum seen so far and update the global maximum if the current path sum is larger.

6. **Return the Maximum Gain**:
   To ensure the recursion continues correctly, return the maximum gain that the current node can pass to its parent. This is the node's value plus the larger of the left or right gain (since we can only pass one direction to the parent).

### Code Explanation:

Here’s the Python code again for reference:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root) -> int:
    pass

# Test Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

# Test Tree 2
root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

# Test Tree 3
root3 = TreeNode(5)
root3.left = TreeNode(4)
root3.right = TreeNode(8)
root3.left.left = TreeNode(11)
root3.left.left.left = TreeNode(7)
root3.left.left.right = TreeNode(2)
root3.right.left = TreeNode(13)
root3.right.right = TreeNode(4)
root3.right.right.right = TreeNode(1)

# You can now pass these roots (root1, root2, root3) to maxPathSum once it's implemented:
# print(maxPathSum(root1))
# print(maxPathSum(root2))
# print(maxPathSum(root3))

```

### Step-by-Step Explanation:

1. **Initialize `max_sum`**:
   We initialize `max_sum` to hold the global maximum path sum. It is initially set to a very small value (`-infinity`) because we want to update it as soon as we find any valid path.

2. **Recursive Function `max_gain(node)`**:
   This function is responsible for:
   - Calculating the maximum gain we can get from each node.
   - Updating the global maximum path sum whenever we find a path that has a higher sum than the current maximum.

3. **Handling Leaf Nodes and Base Case**:
   If the current node is `None` (i.e., an empty subtree), we return a gain of `0`. This ensures that when we hit a leaf node’s child (which is `None`), we don’t add any value to the path sum.

4. **Recursive Calls for Left and Right Gains**:
   For each node, we recursively calculate the maximum gain from its left and right children. If a child has a negative gain (i.e., the subtree rooted at that child has a negative sum), we ignore it by using `max(gain, 0)`.

5. **Calculate the New Path Sum**:
   Once we have the left and right gains, we compute the **new path sum** that passes through the current node. This path includes:
   - The node's value
   - The left gain (if positive)
   - The right gain (if positive)
   
   This gives us the total sum of the path that passes through the current node and possibly its left and right children.

6. **Update the Global Maximum Path Sum**:
   If the **new path sum** (node's value + left gain + right gain) is greater than the current `max_sum`, we update `max_sum`.

7. **Return the Maximum Gain to the Parent**:
   To continue the recursion, the function returns the maximum gain that the current node can contribute to its parent. This gain is calculated as the node’s value plus the maximum of the left or right gain (since only one path can be extended upwards).

### Example Walkthrough:

Let’s walk through the algorithm using the first example:

#### Tree:
```
       -10
      /    \
     9     20
          /  \
         15   7
```

1. Start at the root node `-10`.
2. Recursively calculate the **left gain** from node `9`. Since `9` has no children, the maximum gain from `9` is `9`.
3. Recursively calculate the **right gain** from node `20`. For node `20`:
   - Calculate the **left gain** from node `15`. Since `15` has no children, the maximum gain from `15` is `15`.
   - Calculate the **right gain** from node `7`. Since `7` has no children, the maximum gain from `7` is `7`.
   - The new path sum at node `20` is `20 + 15 + 7 = 42`. This becomes the new `max_sum`.
4. Back at node `-10`, the **left gain** is `9` and the **right gain** is `35` (since `20` contributes a maximum gain of `20 + max(15, 7) = 35`).
   - The new path sum at `-10` is `-10 + 9 + 35 = 34`, which is not larger than `42`, so the maximum remains `42`.
   
The final result is `42`.

### Time Complexity:
- **Time Complexity**: O(n), where `n` is the number of nodes in the tree. We visit each node once during the traversal.
- **Space Complexity**: O(h), where `h` is the height of the tree. This is the space required by the recursion stack. In the worst case, this could be as large as the number of nodes (for a skewed tree).

This algorithm efficiently finds the maximum path sum using a recursive depth-first traversal and ensures we update the maximum path sum at every node.
