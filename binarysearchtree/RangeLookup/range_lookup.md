## Problem Statement

You are given a Binary Search Tree (BST) and an interval [left, right]. Your task is to write a function that returns all the keys in the BST that lie within this interval (inclusive). The keys should be returned in sorted order. The BST is defined such that each node has a `data` attribute containing the key, and `left` and `right` attributes pointing to the left and right children, respectively.

## Function Signature

```python
Interval = collections.namedtuple('Interval', ('left', 'right'))

def range_lookup_in_bst(tree, interval):
    pass
```

### Function Definition

- `tree`: The root node of a BST.
- `interval`: An `Interval` object containing two properties, `left` and `right`, representing the inclusive bounds of the interval.

### Function Calls

```python
# Example tree node definition
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Function to insert nodes into the BST
def insert_into_bst(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = insert_into_bst(root.left, data)
    else:
        root.right = insert_into_bst(root.right, data)
    return root

# Building the BST from a list of values
def build_bst_from_list(values):
    root = None
    for value in values:
        root = insert_into_bst(root, value)
    return root

# Example usage
values = [10, 5, 1, 7, 15, 12, 20]
bst = build_bst_from_list(values)
interval = Interval(5, 15)
result = range_lookup_in_bst(bst, interval)
```

## High-Level Approach

1. **Utilize BST Properties**: Use the properties of the BST to guide the search efficiently. Since the BST maintains an ordered structure, this can help in deciding whether to move left, right, or include a node's value in the result.

2. **Recursive Traversal**: Implement a recursive helper function to traverse the tree. This function will:
   - **Check Node Inclusion**: If a node's value lies within the interval, include it in the result and recursively explore both subtrees.
   - **Prune the Search**: If a node's value is less than the interval's lower bound, only explore the right subtree. If it is greater than the interval's upper bound, only explore the left subtree.

3. **Collect Results**: Collect and return the keys found within the interval in a list, ensuring they are returned in sorted order due to the in-order traversal nature of the recursive approach.
