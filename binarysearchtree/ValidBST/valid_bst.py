#Validate BST
#https://leetcode.com/problems/validate-binary-search-tree/ Sorted Array to Binary Search Tree


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return (root.left.val < root.val if root.left else True) and (root.right.val > root.val if root.right else True) and self.isValidBST(root.left) and self.isValidBST(root.right)
