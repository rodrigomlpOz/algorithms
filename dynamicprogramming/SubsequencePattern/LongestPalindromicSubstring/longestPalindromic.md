### Problem: **Longest Palindromic Substring**

**Problem Statement:**
Given a string `s`, your task is to find the longest contiguous substring that is a palindrome. A **palindrome** is a string that reads the same forwards and backwards.

### Example:

```plaintext
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer since both "bab" and "aba" are palindromic substrings of the same length.
```

```plaintext
Input: s = "cbbd"
Output: "bb"
```

---

### Function Definition:
```python
def longestPalindrome(s: str) -> str:
    """
    Function to find the longest palindromic substring in a given string.

    Args:
    s: str - Input string.

    Returns:
    str - Longest palindromic substring.
    """
```

---

### Function Calls:

```python
# Example 1
s = "babad"
print(longestPalindrome(s))  # Output: "bab" or "aba"

# Example 2
s = "cbbd"
print(longestPalindrome(s))  # Output: "bb"

# Example 3
s = "a"
print(longestPalindrome(s))  # Output: "a"

# Example 4
s = "ac"
print(longestPalindrome(s))  # Output: "a" or "c"
```

---

### High-Level Solution:

This problem can be solved using **Dynamic Programming (DP)** by keeping track of palindromic substrings in a 2D table. The idea is to mark whether a substring `s[i:j]` is a palindrome and to update the maximum-length palindrome found so far.

#### Steps to Solve:

1. **Base Case**: Every single character is a palindrome by itself, so `dp[i][i] = True` for all `i`.

2. **Recursive Case**:
   - If the first and last characters of the substring (`s[i]` and `s[j]`) are equal, then the substring is a palindrome if the substring inside (`s[i+1:j-1]`) is also a palindrome.
   - If the length of the substring is 2 (i.e., `s[i:j] = s[i:j+1]`), check if both characters are the same.

3. **Track the Longest Palindrome**: Keep track of the longest palindrome found as you iterate through the string.

4. **Return the Result**: Return the longest palindromic substring at the end.

---

### Detailed Solution:

```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]  # DP table to store palindromic status
    start = 0  # Starting index of the longest palindrome
    max_length = 1  # Maximum length of the longest palindrome found
    
    # Base case: every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Fill the DP table for substrings of length >= 2
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_length:
                        max_length = length
                        start = i
    
    # Return the longest palindromic substring
    return s[start:start + max_length]
```

---

### Explanation:

1. **DP Table**: The 2D table `dp[i][j]` stores whether the substring `s[i:j+1]` is a palindrome (`True`) or not (`False`).

2. **Filling the Table**:
   - For substrings of length `1`, mark each character as a palindrome.
   - For substrings of length `2` or more, check if the first and last characters are the same (`s[i] == s[j]`) and if the inner substring `s[i+1:j-1]` is also a palindrome.

3. **Track Longest Palindrome**: As the DP table is filled, update the `start` and `max_length` variables to keep track of the longest palindrome found so far.

4. **Return Result**: At the end, the longest palindrome substring is returned based on the `start` and `max_length` values.

---

### Time Complexity:
- **O(n^2)**: The DP table requires us to check all possible substrings of the input string, which leads to an O(n^2) complexity where `n` is the length of the string.

### Space Complexity:
- **O(n^2)**: We use a 2D table to store the palindromic status of each substring.

---

This solution efficiently finds the longest contiguous palindromic substring using dynamic programming. Let me know if you'd like more clarification or further examples!