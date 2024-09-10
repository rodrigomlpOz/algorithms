### Problem: **Palindromic Substrings**

**Problem Statement:**

Given a string `s`, your task is to return the number of **palindromic substrings** in `s`. A **substring** is a contiguous sequence of characters within the string, and a **palindrome** is a string that reads the same forwards and backwards.

Each character in the string is considered a palindromic substring.

### Example:

```plaintext
Input: s = "abc"
Output: 3
Explanation: Three palindromic substrings are "a", "b", and "c".

Input: s = "aaa"
Output: 6
Explanation: Six palindromic substrings are "a", "a", "a", "aa", "aa", and "aaa".
```

### Function Definition:

```python
def countSubstrings(s: str) -> int:
    """
    Function to count the number of palindromic substrings in the input string.

    Args:
    s: str - The input string.

    Returns:
    int - The number of palindromic substrings.
    """
```

### Function Calls:

```python
# Test case 1
s = "abc"
print(countSubstrings(s))  # Output: 3

# Test case 2
s = "aaa"
print(countSubstrings(s))  # Output: 6

# Test case 3
s = "racecar"
print(countSubstrings(s))  # Output: 10
```

### High-Level Solution:

The problem can be solved efficiently using **Dynamic Programming** or **expand-around-center** techniques.

#### Approach 1: **Expand Around Center**

We can use the fact that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center. There are `2n-1` centers to consider in a string of length `n` (every character is a center, and every pair of consecutive characters can be the center of an even-length palindrome).

For each center, we expand outwards as long as the substring remains a palindrome. The time complexity of this approach is **O(n^2)** because we potentially expand around each center for each character.

### Steps:
1. For each center (either a single character or a pair of consecutive characters), expand outward while the characters on both sides of the center are equal.
2. Count each valid expansion as a palindromic substring.

### Detailed Solution:

```python
def countSubstrings(s: str) -> int:
    # Helper function to expand around the center and count palindromes
    def expand_around_center(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    n = len(s)
    result = 0
    
    # Expand around every center (both single character and pairs of characters)
    for i in range(n):
        # Odd-length palindromes (centered on a single character)
        result += expand_around_center(i, i)
        # Even-length palindromes (centered between two characters)
        result += expand_around_center(i, i + 1)
    
    return result
```

### Explanation:

1. **expand_around_center**:
   - This helper function takes two indices (`left` and `right`) and expands outward while the characters at both indices are equal (i.e., while the substring is a palindrome). It counts each valid palindrome.

2. **Main loop**:
   - For each character in the string, we call `expand_around_center` twice:
     - Once with the same index for both `left` and `right` to handle **odd-length palindromes**.
     - Once with `right = left + 1` to handle **even-length palindromes**.

3. **Final count**:
   - We accumulate the number of palindromic substrings from all possible centers.

### Time Complexity:
- **O(n^2)**: For each of the `2n-1` centers, we expand the palindrome outward, which takes linear time in the worst case.

### Space Complexity:
- **O(1)**: Only a few variables are used, and no extra space is required aside from the input string.

---

### Approach 2: **Dynamic Programming (DP)**

We can also solve this problem using a **DP table** to store whether a substring is a palindrome. The DP solution involves filling a 2D table where `dp[i][j]` is `True` if the substring `s[i:j+1]` is a palindrome.

### Dynamic Programming Approach:

1. **Base Case**:
   - All single characters are palindromes (`dp[i][i] = True` for all `i`).
   
2. **Recursive Relation**:
   - For substrings longer than 1 character, `s[i:j+1]` is a palindrome if:
     - The characters at `i` and `j` are the same (`s[i] == s[j]`).
     - The substring `s[i+1:j]` is also a palindrome (`dp[i+1][j-1]` is `True`).


### Explanation:
1. **DP Table**:
   - `dp[i][j] = True` if the substring `s[i:j+1]` is a palindrome.
   
2. **Filling the Table**:
   - We first mark all single characters as palindromes.
   - For substrings of length 2 and greater, we use the recursive relation to check if the substring is a palindrome and update the count.

### Time Complexity:
- **O(n^2)**: We fill the DP table by considering all substrings of length 1 to `n`.

### Space Complexity:
- **O(n^2)**: We use a 2D DP table to store whether each substring is a palindrome.

---

### Summary:
- **Expand Around Center** is the more intuitive and space-efficient solution (O(1) space) for counting palindromic substrings, with a time complexity of **O(n^2)**.
- **Dynamic Programming** is also **O(n^2)** in time but uses **O(n^2)** space. It’s helpful for problems requiring explicit storage of substring information.

Let me know if you'd like further clarifications or a more in-depth explanation of either approach!