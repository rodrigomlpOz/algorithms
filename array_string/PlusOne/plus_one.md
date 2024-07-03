### Problem: Increment an Arbitrary-Precision Integer

Given a non-negative integer represented as an array of digits, where each element in the array contains a single digit, add one to the integer. The digits are stored such that the most significant digit is at the head of the list.

#### Function Signature:
```python
def plus_one(A: List[int]) -> List[int]
```

#### Input:
- `A` (List[int]): A list of integers where each integer is a digit of a non-negative number. The digits are in big-endian order (most significant digit first).

#### Output:
- (List[int]): A list of integers representing the incremented number in the same format.

#### Example:
```python
assert plus_one([1,2,9]) == [1,3,0]
assert plus_one([9,9,9]) == [1,0,0,0]
assert plus_one([0]) == [1]
```

### High-Level Approach:
1. **Initialize Remainder**: Start by initializing a variable `remainder` to 1. This represents the "one" that we need to add to the number.
2. **Iterate in Reverse**: Loop through the array from the least significant digit to the most significant digit.
    - For each digit, add the `remainder` to the current digit.
    - Update the `remainder` by dividing the current digit by 10.
    - Update the current digit by taking the modulo 10 of the sum.
3. **Handle Most Significant Digit**: After the loop, if there is a carry over (i.e., the most significant digit becomes 10), handle it by setting the first digit to 1 and appending a 0 at the end of the list.
4. **Return Result**: The array now represents the incremented number.

This approach ensures that each digit is correctly updated to reflect the addition of one to the entire number. By iterating from the least significant digit to the most significant digit, we efficiently handle any carry-overs that may occur.
