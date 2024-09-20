### Basic Calculator II Problem

#### Problem Statement
Implement a basic calculator to evaluate a simple expression string.

The expression string contains non-negative integers, '+', '-', '*', '/' operators, and empty spaces. The integer division should truncate toward zero.

Given an expression string `s`, evaluate the expression and return its value.

#### Examples
- Input: `"3+2*2"`
  - Output: `7`
- Input: `" 3/2 "`
  - Output: `1`
- Input: `" 3+5 / 2 "`
  - Output: `5`

#### Function Signature
```python
def calculate(s: str) -> int:
```

### Problem Statement

Implement a basic calculator to evaluate a simple expression string.

The expression string contains non-negative integers, '+', '-', '*', '/' operators, and empty spaces. The integer division should truncate toward zero.

Given an expression string `s`, evaluate the expression and return its value.

### Function Signature
```python
def calculate(s: str) -> int:
    ...
```

### Examples
```python
# Example 1:
print(calculate("3+2*2"))  # Output: 7

# Example 2:
print(calculate(" 3/2 "))  # Output: 1

# Example 3:
print(calculate(" 3+5 / 2 "))  # Output: 5
```


### Function Calls
Here's how you would call the `calculate` function with the provided examples:

```python
# Function call for Example 1
print(calculate("3+2*2"))  # Output: 7

# Function call for Example 2
print(calculate(" 3/2 "))  # Output: 1

# Function call for Example 3
print(calculate(" 3+5 / 2 "))  # Output: 5
```

#### High-Level Algorithm
1. **Initialization**:
   - Initialize `num` to store the current number being processed.
   - Initialize `stack` to keep track of numbers and intermediate results.
   - Initialize `sign` to '+' as the default operator.
2. **Iterate Over String**:
   - For each character in the string:
     - If the character is a digit, update `num` to build the current number.
     - If the character is an operator or the last character of the string:
       - Apply the previous `sign` to the current `num` and update the `stack`:
         - If the sign is '+', append `num` to `stack`.
         - If the sign is '-', append `-num` to `stack`.
         - If the sign is '*', pop the top element from `stack`, multiply it by `num`, and append the result back to `stack`.
         - If the sign is '/', pop the top element from `stack`, divide it by `num`, and append the truncated result back to `stack`.
       - Reset `num` to 0 and update `sign` to the current operator.
3. **Final Calculation**:
   - Sum all elements in `stack` to get the final result.
