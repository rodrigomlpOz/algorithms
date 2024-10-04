## Problem Statement

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. Each number in `candidates` may be used an unlimited number of times. The solution set must not contain duplicate combinations, and the combinations can be returned in any order.

## Function Signature

```python
def combination_sum(arr, target):
    pass
```

### Input Parameters

- `arr`: A list of distinct integers representing the candidate numbers.
- `target`: An integer representing the target sum.

### Output

- A list of lists, where each inner list represents a unique combination of numbers from `arr` that sum to `target`.

### Example Inputs and Outputs

```python
# Assuming the combinationSum function is defined

# Test Case 1: candidates = [2, 3, 6, 7], target = 7
print("Test Case 1: Input = [2, 3, 6, 7], target = 7")
print("Output:", combinationSum([2, 3, 6, 7], 7))  
# Expected Output: [[2, 2, 3], [7]]

# Test Case 2: candidates = [2, 3, 5], target = 8
print("\nTest Case 2: Input = [2, 3, 5], target = 8")
print("Output:", combinationSum([2, 3, 5], 8))  
# Expected Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

## High-Level Approach

1. **Backtracking**: Use backtracking to explore all possible combinations of the candidate numbers that sum to the target. The function should consider each candidate number multiple times if necessary.

2. **Recursive Function `recurse`**:
    - **Parameters**:
      - `arr`: The array of candidate numbers.
      - `ans`: The list to store all valid combinations.
      - `temp`: A temporary list representing the current combination being built.
      - `target`: The current target sum to achieve with the remaining numbers.
      - `pos`: The current position in the array, used to prevent revisiting previous elements in the same recursive path.
    - **Process**:
      - If the `target` is less than 0, the current path is invalid, and the function should return.
      - If the `target` equals 0, the current combination (`temp`) is valid and should be added to the result list (`ans`).
      - Otherwise, iterate over the candidate numbers starting from `pos` to avoid duplicate combinations. For each number, add it to `temp`, subtract it from the `target`, and recursively call the function. After exploring that path, remove the number from `temp` to backtrack.

3. **Avoiding Duplicates**: By ensuring that the iteration in each recursive call starts from the current position (`pos`), the function avoids revisiting previous elements, thus preventing duplicate combinations.

### Function Implementation (without the actual code)

The function `combination_sum` initializes the list `ans` to store the results and calls the recursive function `recurse` to explore all possible combinations. The backtracking approach allows the function to build combinations step-by-step and backtrack when necessary, ensuring that all valid combinations are explored without duplicates.
