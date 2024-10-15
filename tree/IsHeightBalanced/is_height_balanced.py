# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None
    if not root.left and not root.right:
        return root
    root.left = invertTree(root.right)
    root.right = invertTree(root.left)
    return root

# Creating the tree:
#       4
#      / \
#     2   7
#    / \ / \
#   1  3 6  9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Call invertTree (to be implemented)
x = invertTree(root)
