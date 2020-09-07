def max_area(arr):
        n = len(arr)
        m = len(arr[0])

        dp = [ [0] * m for _ in range(n)]

        dp[0][0] = arr[0][0]

        for i in range(1, n):
           dp[i][0] = arr[i][0] 
        for j in range(1, m):
           dp[0][j] = arr[0][j] 
        max_ans = float('-inf')
        for i in range(1, n):
           for j in range(1, m):
              if arr[i-1][j] == 1 and arr[i][j-1] == 1:
                    dp[i][j] = (1 + dp[i-1][j-1]) if dp[i-1][j-1] != 0 else dp[i][j]
                    max_ans = max(max_ans, dp[i][j])
        return (max_ans*max_ans)

arr = [
  [1, 0, 1, 0, 0],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0]
]

ans = max_area(arr)
print(ans)
'''
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''