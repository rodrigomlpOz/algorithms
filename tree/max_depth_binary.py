# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxDepth(root):
   if not root:
       return 0
   else:
       return 1 + max(maxDepth(root.left), maxDepth(root.right))
