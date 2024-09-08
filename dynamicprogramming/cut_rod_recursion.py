'''
Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if the length of the rod is 8 and the values of different pieces are given as the following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

C(i) = max{V[k] + C(i-k)}
       1 < k < i
'''
# Returns the best obtainable price for a rod of length n  
# and price[] as prices of different pieces 
def rodCutting(price, n):
    # 1. Define the DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # 2. Fill the DP table
    for i in range(1, n + 1):  # Loop over available piece lengths
        for j in range(1, n + 1):  # Loop over possible rod lengths
            if i <= j:
                # Option 1: Include the piece of length i
                # Option 2: Exclude the piece of length i
                dp[i][j] = max(price[i-1] + dp[i][j-i], dp[i-1][j])
            else:
                # If the piece length is greater than the rod length, we can't include it
                dp[i][j] = dp[i-1][j]
    
    # 3. Return the result stored in dp[n][n]
    return dp[n][n]

# Example test
price = [1, 5, 8, 9, 10, 17, 17, 20]  # Prices for rod lengths from 1 to 8
n = 8  # Total length of the rod
print(rodCutting(price, n))  # Output: 22


    
