### Problem Definition:
You are given two sorted arrays. Your goal is to find the intersection of these arrays, meaning the elements that are present in both arrays. The result should be unique and should appear in sorted order.

### Functional Definition:
1. **Function Name:** `intersection`
2. **Input Parameters:**
   - `arr1` (List of integers): The first sorted list.
   - `arr2` (List of integers): The second sorted list.
   
3. **Output:**
   - A list containing the unique elements that appear in both `arr1` and `arr2`.

4. **Example Call:**
   ```python
   def intersection(arr1, arr2):
      pass
   arr1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
   arr2 = [5, 5, 6, 8, 8, 9, 10, 10]
   result = intersection(arr1, arr2)
   # Output: [5, 6, 8]
   ```

### High-Level Solution:
1. **Two Pointer Approach:**
   - Use two pointers `i` and `j` to traverse the arrays `arr1` and `arr2`.
   - If both pointers point to the same value, add it to the result list if it's not already in the list (i.e., ensure uniqueness).
   - If the value in `arr1` is smaller than `arr2`, increment the pointer for `arr1` (move to the next element).
   - If the value in `arr2` is smaller than `arr1`, increment the pointer for `arr2`.
   - Continue until one of the pointers reaches the end of its array.

2. **Avoid Duplicates:** The solution should handle cases where there are duplicate elements within the arrays by checking if the current element is the same as the previous one before adding it to the result list.
