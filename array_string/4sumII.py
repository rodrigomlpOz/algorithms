'''
Problem

https://leetcode.com/problems/4sum-ii/
'''

import collections
def fourSumCount(A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hash = collections.defaultdict(int)
        for i in A:
            for j in B:
                hash[i+j] += 1


        count = 0
        for i in C:
            for j in D:
                curr_sum = (i + j) * (-1)
                if hash[curr_sum] > 0:
                    count += hash[curr_sum]
        return count
