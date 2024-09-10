def countSubstrings(s: str) -> int:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    
    # Base case: every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
        count += 1
    
    # Fill the dp table
    for length in range(2, n+1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
    
    return count