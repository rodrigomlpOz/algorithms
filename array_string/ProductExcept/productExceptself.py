'''
https://leetcode.com/problems/product-of-array-except-self/
'''
def productExceptSelf(nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in reversed(range(n)):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
