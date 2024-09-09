def LCS(text1, text2):
    """
    Function to calculate the length of the longest common subsequence (LCS) between two strings using 2D dynamic programming.

    Args:
    text1: str - The first string.
    text2: str - The second string.

    Returns:
    int - The length of the longest common subsequence.
    """
    m, n = len(text1), len(text2)
    
    # Step 1: Create the DP table (m+1 x n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Step 2: Fill the DP table using the recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # Characters match, include them in LCS
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Characters do not match, take the maximum LCS so far
    
    # Step 3: Return the value in the bottom-right cell of the table
    return dp[m][n]
