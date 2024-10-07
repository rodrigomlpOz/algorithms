'''
PROBLEM STATEMENT: https://leetcode.com/problems/invert-binary-tree/
    1
   / \
  2   3
 / \ / \
4  5 6  7

'''
import collections
class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def invertTree(root):
    if not root or (not root.left and not root.right):
        return root
    
    # Recursively invert the left and right subtrees
    inv_left = invertTree(root.right)
    inv_right = invertTree(root.left)
    
    # Swap the inverted left and right subtrees
    root.left = inv_left
    root.right = inv_right
    
    return root



root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
result = invert_tree(root)
print(result)

