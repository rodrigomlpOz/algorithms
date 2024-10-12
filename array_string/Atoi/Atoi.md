Sure, here's the problem statement with function signatures in Python, C++, and C#:

---

### Problem Statement: Implement Atoi (String to Integer Conversion)

Implement the `atoi` function, which converts a string to an integer. The function should handle the following cases:

1. Discards leading whitespace characters.
2. Considers an optional sign character ('+' or '-') followed by numerical digits.
3. Stops converting when encountering the first non-digit character after the initial optional sign.
4. Returns `0` if the string does not contain any valid conversion characters.
5. Handles integer overflow and underflow by returning `INT_MAX` (2147483647) or `INT_MIN` (-2147483648), respectively.

#### Function Signatures

**Python:**

```python
def myAtoi(s: str) -> int:
  pass
```


#### Input

- `s`: A string representing the input to be converted.

#### Output

- An integer representing the converted value.

#### Example

```python
# Example 1
s = "42"
print(myAtoi(s))  # Output: 42

# Example 2
s = "   -42"
print(myAtoi(s))  # Output: -42

# Example 3
s = "4193 with words"
print(myAtoi(s))  # Output: 4193

# Example 4
s = "words and 987"
print(myAtoi(s))  # Output: 0

# Example 5
s = "-91283472332"
print(myAtoi(s))  # Output: -2147483648 (INT_MIN)
```

---

#### Explanation

1. **Leading Whitespaces**: The function should ignore any leading whitespace characters until the first non-whitespace character is found.
2. **Sign Handling**: The function should handle an optional '+' or '-' sign. If no sign is present, it is assumed to be positive.
3. **Numeric Conversion**: The function should convert the subsequent numeric characters until a non-numeric character is encountered.
4. **Invalid Input**: If the string does not contain any numeric characters after discarding leading whitespace, the function should return `0`.
5. **Overflow/Underflow**: The function should handle overflow and underflow by returning `INT_MAX` or `INT_MIN` respectively, if the converted number exceeds the range of a 32-bit signed integer.

---

By following the above guidelines, you can implement the `atoi` function to convert a string to an integer while handling various edge cases effectively.
