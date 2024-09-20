Certainly! Here's a comprehensive breakdown of **LeetCode Problem 28: "Find the Index of the First Occurrence in a String"** tailored in **Python**. This includes the **Problem Definition**, **Function Definition**, **Function Calls**, and an expanded **High-Level Solution** that now incorporates the **Sliding Window Approach** alongside other methods.

---

## **Problem Definition**

**Objective:**
Given two strings, `haystack` and `needle`, your task is to find the **starting index** of the **first occurrence** of `needle` within `haystack`. If `needle` is not present in `haystack`, return `-1`.

**Constraints:**
- `1 <= len(haystack), len(needle) <= 10^4`
- Both `haystack` and `needle` consist of only lowercase English characters.

**Examples:**

1. **Example 1:**
   - **Input:** `haystack = "sadbutsad"`, `needle = "sad"`
   - **Output:** `0`
   - **Explanation:** `"sad"` first appears at index `0` in `"sadbutsad"`.

2. **Example 2:**
   - **Input:** `haystack = "leetcode"`, `needle = "leeto"`
   - **Output:** `-1`
   - **Explanation:** `"leeto"` does not appear in `"leetcode"`.

---

## **Function Definition**

In Python, the problem is typically addressed by defining a function named `strStr`. Below is the standard function signature:

```python
def strStr(haystack: str, needle: str) -> int:
    """
    Finds the index of the first occurrence of needle in haystack.

    Parameters:
    haystack (str): The string to search within.
    needle (str): The substring to search for.

    Returns:
    int: The starting index of the first occurrence of needle in haystack, or -1 if not found.
    """
    pass  # Implementation goes here
```

- **Parameters:**
  - `haystack` (str): The string in which to search for the substring.
  - `needle` (str): The substring to search for within `haystack`.

- **Returns:**
  - An integer representing the **starting index** of the first occurrence of `needle` in `haystack`.
  - Returns `-1` if `needle` is not found within `haystack`.

---

## **Function Calls**

Here's how you can call the `strStr` function with different inputs:

1. **Example 1:**

   ```python
   result = strStr("sadbutsad", "sad")
   print(result)  # Expected Output: 0
   ```

2. **Example 2:**

   ```python
   result = strStr("leetcode", "leeto")
   print(result)  # Expected Output: -1
   ```

3. **Additional Example:**

   ```python
   result = strStr("hello", "ll")
   print(result)  # Expected Output: 2
   ```

4. **Edge Case Example (Empty Needle):**

   ```python
   result = strStr("hello", "")
   print(result)  # Expected Output: 0
   ```

--