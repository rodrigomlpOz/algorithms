### Problem Statement
You are given a binary tree with nodes that contain a `parent` pointer, pointing to their parent node. Given two nodes, `node0` and `node1`, find their lowest common ancestor (LCA). The LCA of two nodes is defined as the deepest node that is an ancestor of both nodes.

### Function Definition
Here's the function signature for the problem in Python:

```python
class BinaryTreeNode:
    def __init__(self, data=0, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> BinaryTreeNode:
    # Implementation here
```

### High-Level Solution
1. **Calculate Depths:** Start by determining the depth of both `node0` and `node1` by traversing upwards from each node to the root, counting the number of edges.
2. **Equalize Depths:** If one node is deeper than the other, move up from the deeper node until both nodes are at the same depth.
3. **Find LCA:** Once the depths are equal, move up from both nodes simultaneously until the nodes are the same. The point at which they converge is the LCA.

This method efficiently finds the LCA by leveraging the parent pointers to navigate up the tree.

### Example Function Call
Here’s how you would call the `lca` function and print the result:
```python
node0 = BinaryTreeNode(5)
node1 = BinaryTreeNode(3)
# Assuming node0 and node1 are properly linked in the tree and have a common ancestor
ancestor = lca(node0, node1)
print(f"LCA of node0 and node1 is: {ancestor.data}")
```

This function assumes that both `node0` and `node1` are part of the same tree and that they have a common ancestor.
