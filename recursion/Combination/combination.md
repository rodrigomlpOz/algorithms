**Problem Statement:**

Given two integers `n` and `k`, return all possible combinations of `k` numbers from the range [1, n]. Each combination should be a unique set of `k` numbers, and the order of the numbers within a combination or the order of the combinations themselves does not matter.

**Function Signature:**

```python
def power_set(n: int, k: int):
   pass
```

**Input:**
- `n`: An integer representing the upper limit of the range [1, n].
- `k`: An integer representing the number of elements to choose in each combination.

**Output:**
- A list of lists, where each inner list is a combination of `k` numbers from the range [1, n].

**Examples:**

1. **Example 1:**
   - Input: `n = 4`, `k = 2`
   - Output: `[[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]`

2. **Example 2:**
   - Input: `n = 1`, `k = 1`
   - Output: `[[1]]`

**Constraints:**
- `1 <= n <= 20`
- `1 <= k <= n`

**Explanation:**

The problem requires generating all possible subsets (combinations) of `k` numbers from the set {1, 2, ..., n}. Each combination must contain exactly `k` numbers, and the combinations should be unique, meaning the same set of numbers cannot appear more than once in different orders.

The provided implementation uses a recursive approach to generate combinations:
1. **Recursive Function (`recurse`)**: This function takes the current array, the current list of answers, a temporary list holding the current combination being formed, and the current position in the array.
2. **Base Case**: When the temporary list reaches the desired length `k`, it is added to the answer list.
3. **Recursion**: For each element in the array from the current position, the function adds the element to the temporary list, recursively calls itself to continue building the combination, and then removes the element (backtracks) to explore other possible combinations.

This ensures that all combinations are explored without repetition.
