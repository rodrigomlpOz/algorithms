## Problem Statement

Given an array `nums` of distinct integers, return all possible permutations of the array. The permutations can be returned in any order.

## Function Signature

```python
def permutation(arr):
    pass
```

### Input Parameters

- `arr`: A list of distinct integers.

### Output

- A list of lists, where each inner list represents a unique permutation of the input array.

### Example Inputs and Outputs

**Example 1:**

- **Input:** `nums = [1, 2, 3]`
- **Output:** `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

**Example 2:**

- **Input:** `nums = [0, 1]`
- **Output:** `[[0, 1], [1, 0]]`

**Example 3:**

- **Input:** `nums = [1]`
- **Output:** `[[1]]`

## High-Level Approach

1. **Backtracking**: Use backtracking to generate all possible permutations. The backtracking approach builds each permutation step by step, exploring all potential choices at each step.

2. **Recursive Function `recurse`**:
    - **Parameters**:
      - `arr`: The original array of distinct integers.
      - `ans`: The list to store all permutations.
      - `temp`: A temporary list representing the current permutation being built.
    - **Process**:
      - If the current permutation (`temp`) is complete (i.e., has the same length as `arr`), add it to the result list (`ans`).
      - Otherwise, iterate over each number in the array. If the number is not already in the current permutation (`temp`), add it to `temp` and recursively build further permutations. After exploring that path, remove the number from `temp` to backtrack and try the next number.

3. **Avoiding Duplicates**: The condition `if num in temp` ensures that the same number is not included more than once in a single permutation.


