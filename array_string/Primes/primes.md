## Problem Statement

**Count Primes**

Write a function that returns the number of prime numbers less than a non-negative number, `n`.

**Example:**
```
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```

## High-Level Approach

1. **Initialize a Boolean List**:
    - Create a list `primes` of length `n` where each element is initially set to `True`. This list will be used to mark non-prime numbers.

2. **Mark Non-Prime Numbers**:
    - Starting from the first prime number (2), iterate through the list.
    - For each prime number, mark its multiples as non-prime by setting the corresponding elements in the `primes` list to `False`.

3. **Count the Primes**:
    - Count the number of `True` values in the `primes` list, which indicates the prime numbers less than `n`.

## Function Signature

```python
def count_primes(n):
    pass
```
