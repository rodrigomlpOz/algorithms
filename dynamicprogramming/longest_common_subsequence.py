def lcs(m, n):

    dp = [[0]*(len(m)+1) for _ in range(len(n)+1)]
    for i in range(1, len(n)+1):
        for j in range(1, len(m)+1):
            if n[i-1] == m[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

lcs("abcdaf", "acbcf")