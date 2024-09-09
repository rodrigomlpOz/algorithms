def word_break_2d(s, wordDict):
    """
    2D DP function to determine if the string s can be segmented into words from wordDict.
    
    Args:
    s: str - The input string.
    wordDict: List[str] - The dictionary of valid words.
    
    Returns:
    bool - True if s can be segmented into words from wordDict, False otherwise.
    """
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]  # Step 1: Initialize the DP table

    # Step 2: Initialize the base case for empty substrings
    for i in range(n + 1):
        dp[i][i] = True  # An empty substring can always be segmented

    # Step 3: Fill the DP table for all substrings
    for length in range(1, n + 1):  # Iterate over the length of substrings
        for i in range(n - length + 1):
            j = i + length
            if s[i:j] in wordDict:
                dp[i][j] = True  # Entire substring exists in the dictionary
            else:
                for k in range(i + 1, j):  # Split into two substrings
                    if dp[i][k] and dp[k][j]:
                        dp[i][j] = True
                        break

    # Step 4: Return the result for the full string
    return dp[0][n]
