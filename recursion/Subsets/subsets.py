'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''

def power_set(arr):
    ans = []
    temp = []
    def recurse(arr, ans, temp, pos):
        ans.append(temp[:])
        for i in range(pos, len(arr)):
            temp.append(arr[i])

            recurse(arr, ans, temp, i+1)

            temp.pop()
    recurse(arr, ans, temp, 0)
    return ans
        

arr = [1, 2, 3]
ans = power_set(arr)
print(ans)
