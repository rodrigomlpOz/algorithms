### Problem Statement: Count Four-Sum Combinations

Given four lists of integers `A`, `B`, `C`, and `D`, each of length `n`, you need to compute the number of tuples `(i, j, k, l)` such that:

\[ A[i] + B[j] + C[k] + D[l] = 0 \]

Write a function `fourSumCount` that takes these four lists as input and returns the number of such tuples.

#### Function Signatures

**Python:**

```python
def fourSumCount(A, B, C, D) -> int:
pass
```

#### Input

- `A`, `B`, `C`, `D`: Lists/arrays of integers, each of length \( n \).

#### Output

- An integer representing the number of tuples `(i, j, k, l)` such that \( A[i] + B[j] + C[k] + D[l] = 0 \).

#### Example

```python
# Example 1
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(fourSumCount(A, B, C, D))  # Output: 2

# Example 2
A = [0, 1, -1]
B = [-1, 1, 0]
C = [0, 0, 1]
D = [-1, 1, 1]
print(fourSumCount(A, B, C, D))  # Output: 17

# Example 3
A = [1, 2, 3]
B = [4, -2, -1]
C = [5, -1, 1]
D = [-3, -2, -1]
print(fourSumCount(A, B, C, D))  # Output: 1

# Example 4
A = [0]
B = [0]
C = [0]
D = [0]
print(fourSumCount(A, B, C, D))  # Output: 1
```

---

#### Explanation

1. **Initialize Hash Map**: Create a hash map to store the sum of pairs from lists `A` and `B` and their frequencies.
2. **Count Pairs from C and D**: Iterate over pairs from lists `C` and `D` and check if their negated sum exists in the hash map. If it exists, add the frequency to the count.
3. **Return Count**: Return the total count of such tuples.

This approach leverages the power of hash maps to achieve an efficient solution with a time complexity of \(O(n^2)\).
