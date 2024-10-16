### Problem Statement:
Given two strings `s` and `t`, return `true` if they are **one edit distance** apart, otherwise return `false`.

An **edit distance** between two strings is defined as:
1. **Insert** exactly one character into `s` to get `t`.
2. **Delete** exactly one character from `s` to get `t`.
3. **Replace** exactly one character of `s` with a different character to get `t`.

### Function Definition:
```python
def isOneEditDistance(s: str, t: str) -> bool:
    # Function to determine if two strings are one edit distance apart
    pass
```

### Approach:
1. **Length Difference Check**:
   - If the length difference between `s` and `t` is greater than 1, it's impossible for them to be one edit distance apart, so return `false`.

2. **Iterate and Compare**:
   - If the strings `s` and `t` are of the same length, check for one replacement. If exactly one character is different, return `true`.
   - If the strings `s` and `t` differ by one in length, check for one insertion or deletion.

3. **Return `false`** if none of the conditions match.

### Explanation of the Code:
1. **Length Check**:
   - First, we check if the difference in length between `s` and `t` is greater than 1. If it is, they can't be one edit apart, so we return `False`.
   
2. **Same Length (Replacement Case)**:
   - If `s` and `t` are of the same length, we iterate through both strings, comparing characters. If exactly one character differs, return `True`. If more than one character differs, return `False`.

3. **Different Length (Insert/Delete Case)**:
   - If the length difference between `s` and `t` is exactly 1, we treat it as an insertion or deletion. We compare characters until we find a difference, then check if the remainder of the shorter string matches the longer string after skipping one character from the longer string.

4. **Edge Cases**:
   - If the strings are identical (`""` vs. `""`, or `"abc"` vs. `"abc"`), they are not one edit distance apart, so return `False`.

### Example Walkthrough:

#### Example 1:
```python
s = "ab"
t = "acb"
print(isOneEditDistance(s, t))  # Output: True
Explanation: We can insert 'c' into s to get t.
```

#### Example 2:
```python
s = ""
t = ""
sol = Solution()
print(sol.isOneEditDistance(s, t))  # Output: False
Explanation: Two empty strings are not one edit apart.
```

### Time and Space Complexity:
- **Time Complexity**: O(n), where `n` is the length of the shorter string (`s` or `t`). We iterate through the strings once.
- **Space Complexity**: O(1), as we only use a few variables to keep track of indices and differences.

This solution efficiently checks whether two strings are one edit distance apart using constant space and linear time.
