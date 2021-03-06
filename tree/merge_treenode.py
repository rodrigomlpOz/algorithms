# Definition for a binary tree node.
# class TreeNode:
'''
PROBLEM STATEMENT:
https://leetcode.com/problems/merge-two-binary-trees/
''' 
class Treenode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def mergeTrees(t1, t2):
   if not t1 and not t2:
       return None
   if not t1 or not t2:
       return t1 or t2
   root = TreeNode(t1.val + t2.val)
   root.left = self.mergeTrees(t1.left, t2.left)
   root.right = self.mergeTrees(t1.right, t2.right)
   return root
