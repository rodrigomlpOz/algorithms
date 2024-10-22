### Problem Statement

Given an integer `n`, write a function that generates all combinations of well-formed parentheses with `n` pairs of parentheses.

A well-formed parentheses combination means that every opening parenthesis `'('` has a corresponding closing parenthesis `')'`, and they are placed in a valid order. For example, `"()"`, `"(())"`, and `"()()"` are well-formed combinations, while `"())("` and `"(()"` are not.

### Function Definition

```python
def generateParentheses(n):
    """
    Generates all combinations of well-formed parentheses for n pairs.
    
    Args:
    n (int): The number of pairs of parentheses.
    
    Returns:
    List[str]: A list of strings, each representing a valid combination of parentheses.
    """
    pass  # Implementation goes here
```

### Example Function Calls

```python
# Example 1
n = 3
result = generateParentheses(n)
print(result)
# Expected output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

# Example 2
n = 1
result = generateParentheses(n)
print(result)
# Expected output: ["()"]

# Example 3
n = 0
result = generateParentheses(n)
print(result)
# Expected output: [""]
```

### Requirements:
- The function should return all possible combinations of well-formed parentheses for the given number of pairs.
- The order of the combinations in the output list does not matter.