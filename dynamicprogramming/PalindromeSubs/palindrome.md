### Problem Statement:
Given a string `s`, return the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

### Example:
**Input:**  
`s = "cbbd"`

**Output:**  
`2`

**Explanation:**  
The longest palindromic subsequence is `"bb"`.

---

### Function Definition:

```python
def longest_palindrome_subseque(s):
    """
    Function to find the length of the longest palindromic subsequence in a string.

    Args:
    s: str - Input string.

    Returns:
    int - Length of the longest palindromic subsequence.
    """
    pass  # Placeholder for the actual implementation
```

---

### Function Calls:

```python
# Test Case 1
s = "cbbd"
ans = longest_palindrome_subseque(s)
print(ans)  # Expected output: 2

# Test Case 2
s = "bbbab"
ans = longest_palindrome_subseque(s)
print(ans)  # Expected output: 4 (the longest palindromic subsequence is "bbbb")

# Test Case 3
s = "abcd"
ans = longest_palindrome_subseque(s)
print(ans)  # Expected output: 1 (the longest palindromic subsequence is any single character)
```

---

### Recursive Relation:

To solve this problem using a dynamic programming approach, we use the following recursive relation:

1. **Base Case:**  
   - A single character is always a palindrome of length `1`. Therefore, `dp[i][i] = 1` for all `i`.

2. **Recursive Case:**
   - If the characters at positions `i` and `j` are the same (`s[i] == s[j]`), then they contribute to the palindromic subsequence. Thus, the length of the longest palindromic subsequence is:
     \[
     dp[i][j] = dp[i+1][j-1] + 2
     \]
   - If the characters are not the same (`s[i] != s[j]`), then the longest palindromic subsequence will be the maximum of either:
     - The subsequence obtained by excluding the character at `i`: `dp[i+1][j]`
     - The subsequence obtained by excluding the character at `j`: `dp[i][j-1]`
     \[
     dp[i][j] = \max(dp[i+1][j], dp[i][j-1])
     \]

3. **Final Result:**
   - The length of the longest palindromic subsequence in the entire string `s` is stored in `dp[0][n-1]`, where `n` is the length of the string.

---

### High-Level Process:

1. **Define a DP Table:**
   - Create a 2D DP table `dp[i][j]` where each entry stores the length of the longest palindromic subsequence in the substring `s[i:j+1]`.

2. **Base Case:**
   - Initialize the diagonal of the DP table (`dp[i][i] = 1`), as each single character is a palindrome.

3. **Fill the DP Table:**
   - Use the recursive relation to fill the table from shorter substrings to longer ones.

4. **Return the Final Result:**
   - The final result is the value in `dp[0][n-1]`, which gives the length of the longest palindromic subsequence in the string `s`.

This approach ensures an efficient way to find the longest palindromic subsequence using dynamic programming.
