### Problem Statement:
You are given an array of integers, and your task is to sort this array using a technique called "pancake sorting." Pancake sorting allows you to flip the order of the first `k` elements of the array in a single operation, where `k` can be any number between 1 and the length of the array. Your goal is to sort the array in ascending order using a sequence of these flip operations.

### Functional Definition:
1. **Function Name:** `pancake_sort`
2. **Input Parameters:**
   - `arr` (List of integers): The array that needs to be sorted using pancake sorting.
   
3. **Output:**
   - The function will modify the input array in place, sorting it in ascending order. It also prints the sorted array as the final output.

### Example Call and Run:

Consider the input array:

```python
arr = [5, 2, 3, 1, 4]
```

### Step-by-Step Execution:

1. **Initial Array:**
   - `arr = [5, 2, 3, 1, 4]`

2. **Iteration 1 (i = 4):**
   - Find the maximum value in `arr[0:5]`, which is `5` at index `0`.
   - Flip the array at index `0` (no change).
   - Flip the array at index `4`:
     - `arr = [4, 1, 3, 2, 5]`

3. **Iteration 2 (i = 3):**
   - Find the maximum value in `arr[0:4]`, which is `4` at index `0`.
   - Flip the array at index `0` (no change).
   - Flip the array at index `3`:
     - `arr = [2, 3, 1, 4, 5]`

4. **Iteration 3 (i = 2):**
   - Find the maximum value in `arr[0:3]`, which is `3` at index `1`.
   - Flip the array at index `1`:
     - `arr = [3, 2, 1, 4, 5]`
   - Flip the array at index `2`:
     - `arr = [1, 2, 3, 4, 5]`

5. **Iteration 4 (i = 1):**
   - Find the maximum value in `arr[0:2]`, which is `2` at index `1`.
   - Flip the array at index `1` (no change).

6. **Final Array:**
   - `arr = [1, 2, 3, 4, 5]`

### Output:
The final output after executing the pancake sort is:

```python
[1, 2, 3, 4, 5]
```

This process shows how the pancake sort algorithm works by progressively placing the largest unsorted elements into their correct positions through a series of flips. Each iteration reduces the size of the unsorted portion of the array until the entire array is sorted.
