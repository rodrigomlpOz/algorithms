### Problem Statement:
Given two strings `s` and `p`, where `p` is a **wildcard pattern** that includes the characters `?` and `*`:
- `?` matches any single character.
- `*` matches any sequence of characters (including the empty sequence).

Your task is to implement a function that checks whether the wildcard pattern `p` matches the string `s`.

### Example:
```plaintext
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second character 'a' doesn't match 'b'.

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The pattern '*a*b' matches the string "adceb".

Input: s = "acdcb", p = "a*c?b"
Output: false
```

### Constraints:
- `1 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'?'`, or `'*'`.

### Function Definition:
```python
def isMatch(s: str, p: str) -> bool:
    """
    Function to check if the wildcard pattern p matches the string s.

    Args:
    s: str - The input string.
    p: str - The wildcard pattern.

    Returns:
    bool - True if the pattern matches the string, otherwise False.
    """
```

### Function Calls:
```python
# Test cases
print(isMatch("aa", "a"))         # Output: False
print(isMatch("aa", "*"))         # Output: True
print(isMatch("cb", "?a"))        # Output: False
print(isMatch("adceb", "*a*b"))   # Output: True
print(isMatch("acdcb", "a*c?b"))  # Output: False
```

### High-Level Solution:

We can solve this problem using **dynamic programming (DP)**. The idea is to use a DP table `dp[i][j]`, where:
- `i` represents the current index in string `s`.
- `j` represents the current index in pattern `p`.
- `dp[i][j]` is `True` if the substring `s[:i]` matches the subpattern `p[:j]`.

#### Key Observations:
1. If the current character in the pattern `p[j-1]` is `*`, it can match zero or more characters:
   - Zero characters: Check if the pattern `p[:j-1]` matches the string `s[:i]`.
   - One or more characters: Check if the pattern `p[:j]` matches the string `s[:i-1]` (i.e., treat the current character in `s` as part of the match).
   
2. If the current character in the pattern `p[j-1]` is `?`, it matches any single character from the string `s`.
   
3. If `p[j-1]` is a regular character, it should exactly match `s[i-1]`.

#### Dynamic Programming Table Initialization:
- `dp[0][0] = True`: An empty string matches an empty pattern.
- `dp[i][0] = False`: A non-empty string cannot match an empty pattern.
- `dp[0][j] = True`: If the pattern is non-empty and contains only `*`, it can match an empty string.

#### DP Transition:
- If `p[j-1] == '*': dp[i][j] = dp[i-1][j] or dp[i][j-1]`
- If `p[j-1] == '?' or p[j-1] == s[i-1]: dp[i][j] = dp[i-1][j-1]`


### Time Complexity:
- **O(m * n)**: We fill a DP table of size `m x n`, where `m` is the length of the string `s` and `n` is the length of the pattern `p`.

### Space Complexity:
- **O(m * n)**: We use a DP table of size `(m + 1) x (n + 1)`.

### Explanation of DP Transitions:
1. If we encounter `*`, it can either match zero characters (`dp[i][j-1]`) or one/more characters (`dp[i-1][j]`).
2. If we encounter `?`, it matches any single character (`dp[i-1][j-1]`).
3. If we encounter a regular character, it must match exactly with the character in the string (`dp[i-1][j-1]`).

### Optimizations:
- The space complexity can be reduced to **O(n)** by keeping only two rows of the DP table, since we only need the current and previous row at any time.

Let me know if you'd like to explore that optimization!
