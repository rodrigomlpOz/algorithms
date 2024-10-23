### Problem Statement:
The task is to determine if two strings, `s` and `t`, are isomorphic. Two strings are considered isomorphic if the characters in `s` can be replaced to get `t`, with each character mapping to another character consistently throughout both strings. No two characters in `s` should map to the same character in `t`, and vice versa.

### Function Definition:
```python
def isIsomorphic(s: str, t: str) -> bool:
    """
    Determines if two strings are isomorphic, meaning characters from s can be replaced to get t.
    
    Args:
    s (str): The first string.
    t (str): The second string.
    
    Returns:
    bool: True if s and t are isomorphic, False otherwise.
    """
```

### Function Calls:
```python
# Test case 1: Should return True because 'egg' and 'add' have consistent mappings
print(isIsomorphic("egg", "add"))  # Output: True

# Test case 2: Should return False because 'foo' and 'bar' do not have consistent mappings
print(isIsomorphic("foo", "bar"))  # Output: False

# Test case 3: Should return True because 'paper' and 'title' have consistent mappings
print(isIsomorphic("paper", "title"))  # Output: True

# Test case 4: Should return False because 'abc' and 'defg' have different lengths
print(isIsomorphic("abc", "defg"))  # Output: False
```

### High-Level Solution:
1. **Check for Consistent Mappings:**
   - Use two dictionaries to keep track of character mappings: one for mapping characters from `s` to `t`, and another for mapping characters from `t` to `s`.
   - This is necessary to ensure a one-to-one relationship in both directions (i.e., each character in `s` maps to exactly one character in `t`, and vice versa).

2. **Iterate Through Both Strings Simultaneously:**
   - For each character pair `(char_s, char_t)` from `s` and `t`, check if there are any conflicting mappings:
     - If `char_s` has been mapped to a different character than `char_t` in the past, return `False`.
     - If `char_t` has been mapped to a different character than `char_s` in the past, return `False`.

3. **Create New Mappings When Needed:**
   - If no conflicting mappings are found, add the new character pair `(char_s, char_t)` to the dictionaries.

4. **Return `True` if No Conflicts are Found:**
   - If the iteration completes without returning `False`, it means that the strings are isomorphic.

### Example Walkthrough:

- **Input:** `s = "egg"`, `t = "add"`
  - `map_s_to_t`: {} and `map_t_to_s`: {} (initially empty)
  - Character pairs: ('e', 'a'), ('g', 'd'), ('g', 'd')
  - No conflicts in mapping, so return `True`.

- **Input:** `s = "foo"`, `t = "bar"`
  - `map_s_to_t`: {} and `map_t_to_s`: {} (initially empty)
  - Character pairs: ('f', 'b'), ('o', 'a'), ('o', 'r')
  - Conflict detected for character 'o' mapping to both 'a' and 'r', so return `False`.
