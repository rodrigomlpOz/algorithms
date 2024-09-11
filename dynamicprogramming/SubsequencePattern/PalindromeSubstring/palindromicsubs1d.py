def countSubstrings(s: str) -> int:
    n = len(s)
    count = 0
    
    # Step 1: Initialize a 1D DP array
    dp = [False] * n

    # Step 2: Traverse the string and check for palindromes
    for i in range(n):
        for j in range(i, -1, -1):
            # Step 3: Check if substring s[j:i+1] is a palindrome
            if s[i] == s[j] and (i - j < 2 or dp[j + 1]):
                dp[j] = True
                count += 1
            else:
                dp[j] = False
    
    return count
