def triangle(matrix):
    n = len(matrix)
    m = len(matrix[-1])

    dp = [ [0]*m for _ in range(n)]

    dp[0][0] = matrix[0][0]

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = matrix[i][j] + dp[i-1][j]
            elif i == j:
                dp[i][j] = matrix[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1])
    return min(dp[-1])


coins = [5,25,10,1]