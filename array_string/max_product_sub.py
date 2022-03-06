'''
https://leetcode.com/problems/maximum-product-subarray/
'''

def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #store the result that is the max we have found so far
        global_max = nums[0]
        #// localmax/localmin stores the max/min product of
        #  subarray that ends with the current number A[i]
        local_max = nums[0]
        local_min = nums[0]
        
        for i in range(1, len(nums)):
            # multiplied by a negative makes big number smaller, small number bigger
            #so we redefine the extremums by swapping them
            if nums[i] < 0:
                local_max, local_min = local_min, local_max
            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            local_max = max(nums[i], nums[i]*local_max)
            local_min = min(nums[i], nums[i]*local_min)
            
            #// the newly computed max value is a candidate for our global result
            global_max = max(global_max, local_max)
        
        return global_max
