### Problem Statement:
You are given two strings, `ransomNote` and `magazine`. The goal is to determine if you can construct the `ransomNote` using the letters from the `magazine`. Each letter in the `magazine` can only be used once. Return `True` if it is possible to construct the `ransomNote`, otherwise return `False`.

### Function Definition:
```python
def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if the ransomNote can be constructed from the letters in the magazine.
    
    Args:
    ransomNote (str): The string representing the ransom note.
    magazine (str): The string representing the magazine text.
    
    Returns:
    bool: True if ransomNote can be constructed from magazine, False otherwise.
    """
```

### Function Calls:
```python
# Test case 1: Should return True
print(canConstruct("aabb", "ababc"))  # Output: True

# Test case 2: Should return False
print(canConstruct("aabb", "abac"))   # Output: False

# Test case 3: Should return True
print(canConstruct("hello", "hleollp")) # Output: True

# Test case 4: Should return False
print(canConstruct("hello", "hleol")) # Output: False
```

### High-Level Solution:
1. **Use a Hash Map (Dictionary) to Count Characters:**
   - First, create a dictionary to count the occurrences of each character in the `magazine`. This helps track how many times each character is available for constructing the `ransomNote`.

2. **Iterate Through `ransomNote`:**
   - For each character in the `ransomNote`, check if it is available in the dictionary and if its count is greater than zero. If it is, decrement the count, indicating that one instance of that character has been used. 
   - If a character is either not found in the dictionary or its count is zero, return `False` because there aren't enough characters to form the `ransomNote`.

3. **Return `True` if All Characters Match:**
   - If you successfully check all characters in the `ransomNote` without running out of corresponding characters in the `magazine`, return `True`.

### Example Walkthrough:

- **Input:** `ransomNote = "aabb"`, `magazine = "ababc"`
- **Step 1:** Build the character count for `magazine`:
  - `{ 'a': 2, 'b': 2, 'c': 1 }`
- **Step 2:** Check each character in `ransomNote`:
  - 'a' is available, use one (`a` count becomes 1).
  - 'a' is available again, use one (`a` count becomes 0).
  - 'b' is available, use one (`b` count becomes 1).
  - 'b' is available again, use one (`b` count becomes 0).
- **Result:** All characters in `ransomNote` were successfully matched, so return `True`.
