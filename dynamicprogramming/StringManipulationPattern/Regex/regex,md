### Problem Description:

You are given two strings: `s` (the input string) and `p` (the pattern string), where `p` contains two special characters:
- `.` matches any single character.
- `*` matches zero or more of the preceding element.

Your task is to implement a regular expression matching function that supports these two special characters. The function should return `True` if the pattern `p` matches the entire input string `s`, otherwise return `False`.

### Examples:

1. **Example 1**:
   ```text
   Input: s = "aa", p = "a*"
   Output: True
   Explanation: "*" means zero or more of the preceding element, so "a*" matches "aa".
   ```

2. **Example 2**:
   ```text
   Input: s = "ab", p = ".*"
   Output: True
   Explanation: ".*" means "zero or more (*) of any character (.)", so it matches "ab".
   ```

3. **Example 3**:
   ```text
   Input: s = "aab", p = "c*a*b"
   Output: True
   Explanation: "c*" can be repeated 0 times, "a*" can be repeated 2 times, so it matches "aab".
   ```

### Function Definition:

```python
def isMatch(s: str, p: str) -> bool:
    # Function logic goes here
    pass

# Example calls:
print(isMatch("aa", "a*"))  # Output: True
print(isMatch("ab", ".*"))  # Output: True
print(isMatch("aab", "c*a*b"))  # Output: True
```

---

### High-Level Solution:

To solve this problem, we can use **dynamic programming** (DP). The basic idea is to build a 2D DP table where `dp[i][j]` represents whether the substring `s[:i]` matches the pattern `p[:j]`.

#### Key Points:

1. **Character Match**:
   - If `p[j-1] == s[i-1]` or `p[j-1] == '.'`, it means the current characters match, so we can carry forward the result from the previous substring.
   
2. **Handling `*`**:
   - The `*` character can match zero or more occurrences of the preceding character. This gives us two cases:
     - Match zero occurrences: We ignore the character before `*` and move on (`dp[i][j-2]`).
     - Match one or more occurrences: If the current character in `s` matches the character before `*`, we check if removing one matching character helps (`dp[i-1][j]`).

3. **Base Case**:
   - `dp[0][0] = True`: Both the input string `s` and pattern `p` are empty, so they match.
   - `dp[0][j]`: This handles patterns like `a*`, `a*b*`, etc., which can match an empty string by ignoring parts of the pattern.


### Dynamic Programming Approach:

#### Solution Code:

```python

### Explanation of the DP Approach:

1. **DP Table Setup**:
   - We create a 2D DP table `dp` where `dp[i][j]` represents whether the substring `s[:i]` matches the pattern `p[:j]`. The size of the table is `(len(s) + 1) x (len(p) + 1)`.

2. **Base Case**:
   - `dp[0][0] = True`: Both the string and pattern are empty, so they trivially match.
   - We also handle cases where the pattern can match an empty string, like `a*`, `a*b*`, etc. If the pattern `p` can reduce to an empty string, we set `dp[0][j] = True` for certain values of `j`.

3. **Filling the DP Table**:
   - For each position `(i, j)` in the DP table:
     - **If the characters match**: If `s[i-1] == p[j-1]` or if `p[j-1] == '.'`, set `dp[i][j] = dp[i-1][j-1]`.
     - **If `*` is encountered**: There are two possible actions:
       1. Treat `*` as zero occurrences of the preceding character (`dp[i][j] = dp[i][j-2]`).
       2. If the preceding character matches, treat `*` as one or more occurrences (`dp[i][j] = dp[i-1][j]`).

4. **Final Result**:
   - The result is stored in `dp[len(s)][len(p)]`, which will tell us if the full string matches the full pattern.

---

### Time and Space Complexity:

- **Time Complexity**: `O(m * n)`, where `m` is the length of the string `s` and `n` is the length of the pattern `p`. This is because we iterate through the DP table of size `m x n` and fill each entry in constant time.
  
- **Space Complexity**: `O(m * n)` for storing the DP table.

---

### Example Walkthrough:

1. **Example 1**: `s = "aa", p = "a*"`
   - We can match "a" zero or more times, so the pattern can match "aa". The DP table will result in `True` for the full match.

2. **Example 2**: `s = "ab", p = ".*"`
   - The pattern `.*` can match any character zero or more times, so it matches "ab".

3. **Example 3**: `s = "aab", p = "c*a*b"`
   - The pattern can be reduced to `a*b`, and "aab" matches "a*b", so it returns `True`.

---

This DP approach efficiently handles the complexity of regular expression matching with `.` and `*` operators.
