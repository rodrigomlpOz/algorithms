## Problem Statement

A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For example, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For example, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2. Given a string that consists of brackets, write a function `bracketMatch` that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

## Function Signature

```python
def bracket_match(text: str) -> int:
```

## Function Signature

```python
def bracket_match(text: str) -> int:
```

## Function Calls in Python

To demonstrate how you can use the `bracket_match` function, here are a few example function calls:

```python
# Example 1: Input string is already correctly matched
print(bracket_match("(())()"))  # Expected output: 0

# Example 2: Input string has unmatched opening brackets
print(bracket_match("((("))  # Expected output: 3

# Example 3: Input string has unmatched closing brackets
print(bracket_match(")))"))  # Expected output: 3

# Example 4: Input string has mixed unmatched brackets
print(bracket_match(")("))  # Expected output: 2

# Example 5: Input string with no brackets
print(bracket_match(""))  # Expected output: 0
```

## High-Level Approach

1. **Initialize Counters**:
   - Use two counters, `open_brackets` to count unmatched opening brackets and `close_brackets` to count unmatched closing brackets.

2. **Iterate Through the String**:
   - Traverse each character in the input string.
   - If the character is an opening bracket `(`, increment the `open_brackets` counter.
   - If the character is a closing bracket `)`, check if there is an unmatched opening bracket:
     - If there is, decrement the `open_brackets` counter as you can match this closing bracket with an unmatched opening bracket.
     - If there isn't, increment the `close_brackets` counter as this closing bracket is unmatched.

3. **Calculate the Result**:
   - The result will be the sum of unmatched opening brackets and unmatched closing brackets (`open_brackets + close_brackets`).

This approach ensures that you count all unmatched opening and closing brackets, and the total number of unmatched brackets will be the minimum number needed to add to make the string correctly matched.
