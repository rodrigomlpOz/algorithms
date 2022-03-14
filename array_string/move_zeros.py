'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
 '''
 def moveZeroes(nums):
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1

         
 def moveZeroes(nums):
     lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
               nums[lastNonZeroFoundAt] = nums[i]
               lastNonZeroFoundAt += 1
        
        for j in range(lastNonZeroFoundAt, len(nums)):
              nums[j] = 0;
