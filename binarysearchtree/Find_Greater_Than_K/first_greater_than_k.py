class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def first_greater_than_k(root: TreeNode, k: int) -> int:
    candidate = None
    
    while root:
        if root.val > k:
            # This node is a candidate, but there might be a smaller one
            candidate = root.val
            root = root.left  # Move to the left subtree to look for a smaller value
        else:
            # Move to the right subtree to find larger values
            root = root.right
    
    return candidate

# Example usage:
# Constructing the following BST
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

k = 4
print(first_greater_than_k(root, k))  # Output: 5
