The **Longest Substring Without Repeating Characters** problem asks you to find the length of the longest substring in a given string `s` that contains no repeating characters.

### Problem Example:
- **Input**: `"abcabcbb"`
- **Output**: `3` (The answer is "abc", with the length of 3.)


### Approach: Sliding Window Technique
This problem can be efficiently solved using the **sliding window** technique combined with a **hash set** to track the unique characters in the current window.

1. **Initialize two pointers**: `left` and `right`, both starting at the beginning of the string.
2. **Expand the window**: Move the `right` pointer to the right, adding characters to a hash set as long as there are no duplicates.
3. **Shrink the window**: When a duplicate is encountered, move the `left` pointer to remove characters until the duplicate is eliminated.
4. **Track the maximum length**: Keep updating the length of the longest substring encountered.

### Why while loop?

Example:
Consider the string "abba" and the sliding window approach:

When the right pointer reaches the second 'b', an if statement would remove only the first character, but the substring would still have repeating 'b's.
The while loop ensures that both characters ('a' and 'b') are removed until the substring becomes valid again (i.e., the second 'b' can now be added).

### Python Code Example:

```python
# Function definition
def lengthOfLongestSubstring(s: str) -> int:
    pass

# Test Case 1: Regular case with repeating characters
s1 = "abcabcbb"
print(lengthOfLongestSubstring(s1))  # Expected output: 3 ("abc")

# Test Case 2: String with all unique characters
s2 = "abcdefg"
print(lengthOfLongestSubstring(s2))  # Expected output: 7 ("abcdefg")

# Test Case 3: String with all same characters
s3 = "bbbbbb"
print(lengthOfLongestSubstring(s3))  # Expected output: 1 ("b")

# Test Case 4: String with mixed characters
s4 = "pwwkew"
print(lengthOfLongestSubstring(s4))  # Expected output: 3 ("wke")

# Test Case 5: Empty string
s5 = ""
print(lengthOfLongestSubstring(s5))  # Expected output: 0 (No substring)

# Test Case 6: Single character string
s6 = "z"
print(lengthOfLongestSubstring(s6))  # Expected output: 1 ("z")

```

### Explanation:
- **Time Complexity**: O(n), where `n` is the length of the string. Each character is added and removed from the set at most once.
- **Space Complexity**: O(min(n, m)), where `m` is the size of the character set, which can be 26 for the alphabet or more for Unicode.

For more detailed explanations and solutions, you can check the LeetCode page [here](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)【48†source】【49†source】.
