class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_largest(root: TreeNode, k: int) -> int:
    # To keep track of the count of visited nodes
    count = 0
    result = None
    
    # Helper function for reverse in-order traversal
    def reverse_inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return
        
        # Traverse the right subtree first
        reverse_inorder(node.right)
        
        # Visit the current node
        count += 1
        if count == k:
            result = node.val
            return
        
        # Traverse the left subtree
        reverse_inorder(node.left)
    
    reverse_inorder(root)
    return result

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

k = 2
print(kth_largest(root, k))  # Output: 5
