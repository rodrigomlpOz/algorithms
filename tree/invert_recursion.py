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
    if not root:
         return None
    left = self.invertTree(root.left)
    right =  self.invertTree(root.right)
    root.left, root.right = right, left
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

