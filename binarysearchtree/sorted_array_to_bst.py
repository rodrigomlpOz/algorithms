'''
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''
class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
def sorted_array_to_bst(nums):
    if not nums:
        return 
    else:
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = sorted_array_to_bst(nums[:mid])
        root.right = sorted_array_to_bst(nums[mid+1:])
        return root
nums = [-10,-3,0,5,9]
sorted_array_to_bst(nums)
