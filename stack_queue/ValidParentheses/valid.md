### Problem Statement: Well-Formed Parentheses

Given a string `s` containing only the characters `'(', ')', '{', '}', '[', ']'`, determine if the string is **well-formed**. A string is well-formed if:
1. Every opening bracket has a corresponding closing bracket of the same type.
2. Brackets are closed in the correct order (i.e., no mismatched or improperly nested brackets).

You need to return `True` if the string is well-formed, otherwise return `False`.

### Function Definition:
```python
def is_well_formed(s):
    """
    Determines if a string of parentheses is well-formed.
    
    Args:
    s (str): The input string consisting of '(', ')', '{', '}', '[', ']'.
    
    Returns:
    bool: True if the string is well-formed, otherwise False.
    """
    pass
```

### Function Calls:
```python
# Test Case 1: Balanced parentheses
s1 = "({[]})"
print(f"Input: {s1} -> Output: {is_well_formed(s1)}")
# Expected Output: True

# Test Case 2: Mismatched parentheses
s2 = "([)]"
print(f"Input: {s2} -> Output: {is_well_formed(s2)}")
# Expected Output: False

# Test Case 3: Incomplete parentheses
s3 = "(]"
print(f"Input: {s3} -> Output: {is_well_formed(s3)}")
# Expected Output: False

# Test Case 4: Single type of parentheses, balanced
s4 = "()[]{}"
print(f"Input: {s4} -> Output: {is_well_formed(s4)}")
# Expected Output: True

# Test Case 5: Empty string
s5 = ""
print(f"Input: {s5} -> Output: {is_well_formed(s5)}")
# Expected Output: True
```

### High-Level Solution:

1. **Stack Data Structure:** Use a stack to keep track of opening brackets as they are encountered.
   - **Why a stack?** A stack follows a "Last In, First Out" (LIFO) approach, which is ideal for handling nested structures like parentheses.

2. **Traverse the String:**
   - For each character in the string:
     - If it's an opening bracket (`'('`, `'{'`, `'['`), push it onto the stack.
     - If it's a closing bracket (`')'`, `'}'`, `']'`), check if it matches the last opening bracket from the stack:
       - If the stack is empty (no opening bracket to match) or the bracket types don't match, return `False`.
       - Otherwise, pop the last opening bracket from the stack.
   
3. **Final Check:**
   - After iterating through the string, if the stack is empty, all brackets were matched properly, so return `True`.
   - If there are unmatched opening brackets left in the stack, return `False`.

This approach ensures that all opening brackets are correctly matched with their corresponding closing brackets, and any mismatches or improperly nested brackets are detected.