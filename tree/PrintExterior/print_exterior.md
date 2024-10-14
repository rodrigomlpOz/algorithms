**Problem Statement:**

Given a binary tree, print its boundary nodes in an anti-clockwise direction starting from the root. The boundary includes the nodes along the left boundary (excluding leaves), all the leaf nodes, and the nodes along the right boundary (excluding leaves).

**Input:**

- A binary tree with nodes having the following structure:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function signature for printExterior
def printExterior(root):
    # TODO: Implement logic to print the exterior nodes of the tree
    pass

# Creating the tree based on the provided structure
root = Node(20)
root.left = Node(8)
root.right = Node(22)

root.left.left = Node(4)
root.left.right = Node(12)

root.left.right.left = Node(10)
root.left.right.right = Node(14)

root.right.right = Node(25)
```

- The tree is defined by a root node that provides access to the entire structure.

**Output:**

- A sequence of integers representing the data values of the boundary nodes in the following order:
  1. Root node
  2. Left boundary nodes (excluding leaf nodes), in top-down order
  3. All leaf nodes, from left to right
  4. Right boundary nodes (excluding leaf nodes), in bottom-up order

**Constraints:**

- The tree can have any structure, including being empty or consisting of a single node.
- Nodes have unique values for simplicity.

**Example:**

Consider the following binary tree:

```
        20
       /  \
      8    22
     / \     \
    4  12     25
       / \
      10  14
```

For this tree, the boundary traversal would output:

```
20 8 4 10 14 25 22
```

Explanation:
- Root node: 20
- Left boundary: 8, 4 (excluding leaves)
- Leaf nodes: 4, 10, 14, 25
- Right boundary: 22 (excluding leaves, in bottom-up order)
