## Problem Statement

Given an array `nums` of unique integers, return all possible subsets (the power set). The solution set must not contain duplicate subsets. The subsets can be returned in any order.

## Function Signature

```python
def power_set(arr):
    pass
```

### Input Parameters

- `arr`: A list of unique integers.

### Output

- A list of lists, where each inner list represents a subset of the input array.

### Example Inputs and Outputs

**Example 1:**

- **Input:** `nums = [1, 2, 3]`
- **Output:** `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`

**Example 2:**

- **Input:** `nums = [0]`
- **Output:** `[[], [0]]`

## High-Level Approach

1. **Backtracking**: Use backtracking to explore all possible subsets. Start with an empty subset and recursively add elements from the array, either including or excluding each element.

2. **Recursive Function `recurse`**:
    - **Parameters**:
      - `arr`: The original array.
      - `ans`: The list to store all subsets.
      - `temp`: A temporary list representing the current subset.
      - `pos`: The current position in the array.
    - **Process**:
      - Add the current subset (`temp`) to the answer list (`ans`).
      - Iterate over the remaining elements in the array starting from the current position.
      - For each element, include it in the current subset, recursively generate further subsets, and then backtrack by removing the element from the current subset.

3. **Backtracking Logic**: After adding an element to the subset, explore further elements by incrementing the position. After exploring all possibilities with the current element, remove it from the subset to explore other subsets that do not include the element (backtracking).

### Function Calls and Example

```python
arr = [1, 2, 3]
ans = power_set(arr)
print(ans)  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

In this example, `power_set` generates all possible subsets of the array `[1, 2, 3]`, including the empty set and the set containing all elements. Each subset is represented as a list within the output list.
