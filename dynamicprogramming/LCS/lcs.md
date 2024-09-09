### Problem Definition (Longest Common Subsequence - LCS):
Given two strings `text1` and `text2`, the task is to find the length of their **longest common subsequence**. A subsequence is a sequence that appears in the same relative order in both strings but not necessarily consecutively. We want to return the length of the longest subsequence that is common to both strings.

### Example 1:
**Input:**  
- `text1 = "abcde"`
- `text2 = "ace"`

**Output:** `3`

**Explanation:**  
The longest common subsequence is `"ace"`, which has a length of `3`.

### Example 2:
**Input:**  
- `text1 = "abc"`
- `text2 = "abc"`

**Output:** `3`

**Explanation:**  
The longest common subsequence is `"abc"`, which has a length of `3`.

### Example 3:
**Input:**  
- `text1 = "abc"`
- `text2 = "def"`

**Output:** `0`

**Explanation:**  
There is no common subsequence, so the result is `0`.

---

### Function Definition:
```python
def LCS(text1, text2):
    """
    Function to calculate the length of the longest common subsequence (LCS) between two strings.

    Args:
    text1: str - The first string.
    text2: str - The second string.

    Returns:
    int - The length of the longest common subsequence.
    """
    # High-level approach will be recursive:
    # 1. Base case: If either string is empty, return 0.
    # 2. If the first characters of both strings match, 
    #    the LCS includes this character and we recurse on the remaining parts.
    # 3. If the first characters do not match, we explore both possibilities:
    #    a. Exclude the first character of text1
    #    b. Exclude the first character of text2
    #    Take the maximum of both recursive results.
    pass  # Placeholder for the actual implementation
```

### Function Calls:
```python
# Test Case 1
text1 = "abcde"
text2 = "ace"
ans = LCS(text1, text2)
print(ans)  # Expected output: 3

# Test Case 2
text1 = "abc"
text2 = "abc"
ans = LCS(text1, text2)
print(ans)  # Expected output: 3

# Test Case 3
text1 = "abc"
text2 = "def"
ans = LCS(text1, text2)
print(ans)  # Expected output: 0
```

---

### High-Level Recursive Approach:

1. **Base Case:**
   - If either `text1` or `text2` is empty, the longest common subsequence is `0` since no common subsequence can exist.

2. **Matching Characters:**
   - If the first characters of `text1` and `text2` match, they are part of the LCS. Add `1` to the result and solve the subproblem for the remaining parts of both strings.

3. **Non-Matching Characters:**
   - If the first characters do not match, explore two possibilities:
     1. Exclude the first character of `text1` and compute the LCS for the remaining part of `text1` and all of `text2`.
     2. Exclude the first character of `text2` and compute the LCS for all of `text1` and the remaining part of `text2`.
   - Return the maximum result from these two options.

4. **Final Result:**
   - The recursive process will eventually explore all valid subsequences and return the length of the longest subsequence found in both `text1` and `text2`.

This structure gives a clear roadmap to implement the recursive LCS function! Let me know if you'd like to go deeper into dynamic programming or optimization.
