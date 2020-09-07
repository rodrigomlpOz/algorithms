def change(amount, coins):
    n = len(coins)
    M = [[0 for i in range(amount+1)] for x in range(n+1)]
    for i in range(n+1):
        M[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, amount+1):
           if coins[i-1] > j:
                M[i][j] = M[i-1][j]
           else:
                M[i][j] = M[i-1][j] + M[i][j-coins[i-1]]
           return M[n][amount]