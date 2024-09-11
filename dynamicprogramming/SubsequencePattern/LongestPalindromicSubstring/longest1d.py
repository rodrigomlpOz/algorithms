def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    dp = [False] * n  # DP array to store palindromic status for the current substring
    start = 0  # Starting index of the longest palindrome
    max_length = 1  # Maximum length of the longest palindrome found
    
    for i in range(n):  # Base case: every single character is a palindrome
        dp[i] = True
    
    # Fill the DP array for substrings of length >= 2
    for length in range(2, n + 1):
        new_dp = [False] * n  # New DP array for the current length of substrings
        for i in range(n - length + 1):
            j = i + length - 1  # End index of the current substring
            
            if s[i] == s[j]:  # If the characters at the start and end match
                if length == 2 or dp[i + 1]:  # If it's two characters or the inner substring is a palindrome
                    new_dp[i] = True
                    if length > max_length:  # Update the longest palindrome if necessary
                        max_length = length
                        start = i
        dp = new_dp  # Update the DP array to the new state

    # Return the longest palindromic substring
    return s[start:start + max_length]

# Example usage:
s = "babad"
print(longestPalindrome(s))  # Output could be "bab" or "aba"
