### Problem Statement:
Given two strings `s` and `t`, return `true` if they are anagrams of each other, otherwise return `false`. An anagram contains the same characters, but they can appear in any order.

### Function Definition:
```python
def is_anagram(s: str, t: str) -> bool:
    # Function to check if two strings are anagrams
```

### Examples:
#### Example 1:
```python
s = "racecar"
t = "carrace"
print(is_anagram(s, t))  # Output: True
```

#### Example 2:
```python
s = "jar"
t = "jam"
print(is_anagram(s, t))  # Output: False
```

### Constraints:
- `s` and `t` consist of lowercase English letters only.

### High-Level Description:
1. **Objective**: Check if two strings contain the same characters with the same frequency.
2. **Approach**:
   - If the lengths of `s` and `t` are different, they can't be anagrams.
   - Count the frequency of each character in both strings and compare the counts.
   - If the character counts are the same, return `true`; otherwise, return `false`.
3. **Efficiency**:
   - Time Complexity: O(n), where `n` is the length of the strings `s` and `t`.
   - Space Complexity: O(1) since we only use a fixed-size array (or dictionary) to store character frequencies (for lowercase English letters, the array size is 26).

### Solution Using Frequency Count (Efficient Approach):
We can use a list of size 26 (for lowercase letters) to count the occurrences of each character in both strings. Then, we compare the two lists.

### Code:

```python
def is_anagram(s: str, t: str) -> bool:
    # If the lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Create a frequency array for both strings
    count_s = [0] * 26
    count_t = [0] * 26
    
    # Update the frequency arrays based on characters in s and t
    for char in s:
        count_s[ord(char) - ord('a')] += 1
    for char in t:
        count_t[ord(char) - ord('a')] += 1
    
    # Compare the frequency arrays
    return count_s == count_t
```

### Example Usage:

#### Example 1:
```python
s = "racecar"
t = "carrace"
print(is_anagram(s, t))  # Output: True
```

#### Example 2:
```python
s = "jar"
t = "jam"
print(is_anagram(s, t))  # Output: False
```

### Explanation of the Code:
1. **Check lengths**: If the strings are of different lengths, they can't be anagrams.
2. **Character count**: We create two arrays of size 26, one for each string, to store the frequency of each character.
3. **Compare counts**: After populating the arrays with character counts, we simply compare them. If they match, the strings are anagrams.

This approach efficiently handles the problem with O(n) time complexity, where `n` is the length of the input strings.
