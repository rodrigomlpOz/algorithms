### Problem Statement

Given two strings `s` and `t`, return the shortest substring of `s` such that every character in `t` (including duplicates) is present in the substring. If such a substring does not exist, return an empty string `""`. You can assume that the output will always be unique.

### Function Definition

```python
def minWindow(s: str, t: str) -> str:
    pass
```

### Function Calls

```python
# Example 1
s = "OUZODYXAZV"
t = "XYZ"
print(minWindow(s, t))  # Output: "YXAZ"

# Example 2
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # Output: "BANC"

# Example 3
s = "a"
t = "a"
print(minWindow(s, t))  # Output: "a"

# Example 4
s = "a"
t = "aa"
print(minWindow(s, t))  # Output: "" (not possible)
```

### High-Level Solution

The **Minimum Window Substring** problem is efficiently solved using the **sliding window** technique along with character frequency counting. Here's a breakdown of the approach:

1. **Character Frequency Map**: First, create a frequency map (a dictionary or `Counter`) for the characters in `t`. This helps track how many of each character we need in the substring.

2. **Sliding Window**: Use two pointers (`left` and `right`) to form a sliding window over the string `s`. Expand the window by moving `right`, and when the window contains all characters of `t`, try shrinking it by moving `left`.

3. **Valid Window Check**: A window is valid if all characters in `t` are present in the window with their required counts.

4. **Tracking the Smallest Window**: While shrinking the window, keep track of the smallest valid window found so far. Update this whenever a smaller valid window is found.

5. **Edge Cases**: If no valid window is found, return an empty string `""`.

### Detailed Solution

```python
from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    pass
```

### High-Level Steps

1. **Initialize Frequency Map**: Create a `Counter` to store the frequency of characters in `t`.
   
2. **Sliding Window Logic**: 
   - Expand the window by moving `right` and add characters to the window count.
   - Once all characters from `t` are in the window, try to shrink the window by moving `left`.
   
3. **Track Smallest Window**: Each time a valid window is found, check if it's the smallest and update the result accordingly.

4. **Edge Handling**: If no valid window is found, return an empty string.

This approach ensures that the solution works efficiently with a time complexity of **O(n)**, where `n` is the length of string `s`. The space complexity is **O(1)** if you only consider the fixed alphabet size, but generally it's **O(n + m)** where `m` is the length of `t`.