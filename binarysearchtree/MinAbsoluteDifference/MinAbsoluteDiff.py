from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Inserts a value into the BST.

    :param root: TreeNode or None, the root of the BST
    :param val: int, the value to insert
    :return: TreeNode, the root of the BST after insertion
    """
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def get_minimum_difference(root: Optional[TreeNode]) -> int:
    """
    Computes the minimum absolute difference between values of any two nodes in a BST.

    :param root: TreeNode or None, the root of the BST
    :return: int, the minimum absolute difference
    """
    prev = None
    min_diff = float('inf')

    def in_order(node: Optional[TreeNode]):
        nonlocal prev, min_diff
        if node is None:
            return
        # Traverse the left subtree
        in_order(node.left)
        # Process the current node
        #Why the Check?: For the first node, there is no previous node to compare with. Attempting to compute node.val - prev when prev is None would result in a TypeError because you cannot perform arithmetic operations between an int and NoneType.
        if prev is not None:
            current_diff = node.val - prev
            min_diff = min(min_diff, current_diff)
        prev = node.val
        # Traverse the right subtree
        in_order(node.right)

    in_order(root)
    return min_diff

# Example Usage
if __name__ == "__main__":
    # Construct the BST
    #       4
    #      / \
    #     2   6
    #    / \
    #   1   3

    values = [4, 2, 6, 1, 3]
    root = None
    for val in values:
        root = insert_into_bst(root, val)

    # Compute the minimum absolute difference
    min_diff = get_minimum_difference(root)
    print(f"The minimum absolute difference is: {min_diff}")  # Output: 1
