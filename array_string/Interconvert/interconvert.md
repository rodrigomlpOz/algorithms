### Problem 1: Integer to String Conversion

Write a function that converts an integer to its corresponding string representation without using built-in string conversion functions.

#### Function Signature:
```python
def int_to_string(num: int) -> str
```

#### Input:
- `num` (int): An integer which can be negative, zero, or positive.

#### Output:
- (str): The string representation of the input integer.


```python
print(int_to_string(345))    # Expected output: "345"
print(int_to_string(-345))   # Expected output: "-345"
print(int_to_string(0))      # Expected output: "0"
``` 

These will directly print the results of `int_to_string()` for each input.

#### High-Level Approach:
1. **Handle Negative Numbers**: Check if the input integer is negative. If so, set a flag and convert the number to its positive equivalent.
2. **Convert Digits to Characters**: Use a loop to repeatedly extract the last digit of the number (using modulo 10), convert it to the corresponding character (using ASCII values), and append it to a result list.
3. **Reconstruct the Number String**: Reverse the result list to get the correct order of digits.
4. **Add Negative Sign**: If the original number was negative, prepend a '-' sign to the result.
5. **Handle Zero**: Special case for zero since the loop won't run for zero.

### Problem 2: String to Integer Conversion

Write a function that converts a string representation of an integer back to its integer form without using built-in integer conversion functions.

#### Function Signature:
```python
def string_to_int(num: str) -> int
```

#### Input:
- `num` (str): A string representing an integer which can be negative, zero, or positive.

#### Output:
- (int): The integer value of the input string.

#### Example:
```python
assert string_to_int("365") == 365
assert string_to_int("-365") == -365
assert string_to_int("0") == 0
```

#### High-Level Approach:
1. **Handle Negative Numbers**: Check if the string starts with a '-' sign. If so, set a flag and process the remaining characters.
2. **Initialize Result**: Start with an integer value of zero.
3. **Convert Characters to Digits**: Iterate over each character in the string, convert it to the corresponding digit (using the position in the ASCII table), and update the result by shifting the current result left (multiply by 10) and adding the new digit.
4. **Apply Negative Sign**: If the original string had a '-', convert the result to its negative equivalent.
5. **Handle Zero**: Ensure the string "0" is correctly converted to the integer 0.

Implementing these functions from scratch without relying on Python's built-in conversion functions will deepen your understanding of how these operations work under the hood.
