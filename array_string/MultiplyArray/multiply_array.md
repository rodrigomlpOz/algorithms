## Problem Statement

**Multiply Two Arbitrary-Precision Integers**

Given two lists representing non-negative integers where each element in the list is a digit, multiply the two integers and return the product as a list of digits.

The digits are stored such that the most significant digit is at the beginning of the list.

**Example:**
```
Input: num1 = [1, 2, 3], num2 = [4, 5, 6]
Output: [5, 6, 0, 8, 8]
Explanation: 123 * 456 = 56088
```

## High-Level Approach

1. **Determine the Sign of the Result**:
    - Check if the two numbers have different signs. If they do, the result will be negative.

2. **Convert to Absolute Values**:
    - Convert both numbers to their absolute values to simplify the multiplication process.

3. **Initialize Result Array**:
    - Create an array `result` with a length equal to the sum of the lengths of the two input numbers. This array will hold the intermediate multiplication results.

4. **Multiply Each Digit**:
    - Iterate through each digit of the first number and multiply it with each digit of the second number.
    - Accumulate the results in the appropriate positions of the `result` array.
    - Handle carry-over for each position.

5. **Remove Leading Zeros**:
    - Strip any leading zeros from the result array.

6. **Apply the Sign**:
    - Apply the determined sign to the most significant digit of the result.

7. **Return the Result**:
    - Return the processed result array.

## Function Signature

```python
def multiply(num1, num2):
    pass
```
