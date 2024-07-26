'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
'''

def power_set(n, k):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    ans = []
    temp = []
    def recurse(arr, ans, temp, pos):
        if len(temp) == k:
            ans.append(temp[:])
        for i in range(pos, len(arr)):
            temp.append(arr[i])

            recurse(arr, ans, temp, i+1)

            temp.pop()
    recurse(arr, ans, temp, 0)
    return ans
        

n = 4
k = 2
ans = power_set(n, k)
print(ans)
