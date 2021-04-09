# Sorted array to BST https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        else:
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:]) 
            return root
