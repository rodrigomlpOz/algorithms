'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''
def permutation(arr):
    ans = []
    temp = []
    def recurse(arr, ans, temp):
        if len(temp) == len(arr):
            ans.append(temp[:])
        for num in arr:
            if num in temp:
                continue
                
            temp.append(num)
            
            recurse(arr, ans, temp)

            temp.pop()
    recurse(arr, ans, temp)
    return ans
        

arr = [1,2,3]
ans = permutation(arr)
print(ans)
