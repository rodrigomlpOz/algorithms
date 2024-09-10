def editDistance(str1, str2):
    """
    A function to calculate the minimum edit distance between two strings using 2D DP.

    Args:
    str1 : str : The first string.
    str2 : str : The second string.

    Returns:
    int : The minimum number of edit operations required to convert str1 to str2.
    """
    m = len(str1)
    n = len(str2)
    
    # 1. Define the DP table (m+1 rows for str1, n+1 columns for str2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # 2. Initialize the DP table
    # If str1 is empty, all characters of str2 must be inserted
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting all characters from str1
    
    # If str2 is empty, all characters of str1 must be deleted
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting all characters of str2

    # 3. Fill the DP table using the recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:  # If characters match, no change
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i][j - 1] + 1,    # Insertion
                    dp[i - 1][j] + 1,    # Deletion
                    dp[i - 1][j - 1] + 1 # Substitution
                )

    # 4. Return the result in dp[m][n]
    return dp[m][n]
