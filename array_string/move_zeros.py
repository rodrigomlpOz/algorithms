'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
 '''
 def moveZeroes(nums):
       anchor = 0
       for explorer in range(len(nums)):
           if nums[explorer] != 0:
               nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
               anchor += 1
