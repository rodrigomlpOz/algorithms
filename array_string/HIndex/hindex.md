### Problem Statement:
Given an array of integers `citations`, where `citations[i]` is the number of citations a researcher received for their ith paper, return the researcher's **h-index**. 

The **h-index** is defined as the maximum value `h` such that the researcher has published at least `h` papers that have each been cited at least `h` times.

### Function Definition:
```python
def hIndex(citations: list[int]) -> int:
    # Function to calculate the h-index of a researcher
```

### Approach:
1. **Sort the citations**: First, sort the citations in descending order. This allows us to count how many papers have at least `h` citations.
2. **Find the maximum h-index**: For each paper, if the number of papers that have more citations than the current value `h` is greater than or equal to `h`, then it qualifies as an h-index.

### Example 1:
```python
citations = [3, 0, 6, 1, 5]
# The researcher has 5 papers, with citation counts [3, 0, 6, 1, 5].
# After sorting: [6, 5, 3, 1, 0]
# The h-index is 3, since there are 3 papers with at least 3 citations.
```

### Example 2:
```python
citations = [1, 3, 1]
# After sorting: [3, 1, 1]
# The h-index is 1, since there is 1 paper with at least 1 citation.
```

### Function Calls:
```python
# Example 1
solution = Solution()
citations1 = [3, 0, 6, 1, 5]
print(solution.hIndex(citations1))  # Output: 3

# Example 2
citations2 = [1, 3, 1]
print(solution.hIndex(citations2))  # Output: 1
```

### Explanation:
1. Sort the citations in descending order.
2. For each paper, check if the number of papers that have at least `i + 1` citations is greater than or equal to the value of `i + 1`.
3. Return the largest such value of `h` (h-index).


Let's illustrate each iteration with the sorted citation array and show how the h-index is computed step by step.

### **Given Array:**
```python
citations = [10, 8, 5, 4, 3]
```

### **Sorted Array:**
```python
citations = [10, 8, 5, 4, 3]
```

### **Iteration Breakdown:**

1. **Iteration 1:**
   - **Citation Array:** `[10, 8, 5, 4, 3]`
   - **Index (`i`):** 0
   - **Citation Count (`num`):** 10
   - **`i + 1`:** 1
   - **Condition (`num >= i + 1`):** `10 >= 1` → **True**
   - **h-index:** 1
   
2. **Iteration 2:**
   - **Citation Array:** `[10, 8, 5, 4, 3]`
   - **Index (`i`):** 1
   - **Citation Count (`num`):** 8
   - **`i + 1`:** 2
   - **Condition (`num >= i + 1`):** `8 >= 2` → **True**
   - **h-index:** 2

3. **Iteration 3:**
   - **Citation Array:** `[10, 8, 5, 4, 3]`
   - **Index (`i`):** 2
   - **Citation Count (`num`):** 5
   - **`i + 1`:** 3
   - **Condition (`num >= i + 1`):** `5 >= 3` → **True**
   - **h-index:** 3

4. **Iteration 4:**
   - **Citation Array:** `[10, 8, 5, 4, 3]`
   - **Index (`i`):** 3
   - **Citation Count (`num`):** 4
   - **`i + 1`:** 4
   - **Condition (`num >= i + 1`):** `4 >= 4` → **True**
   - **h-index:** 4

5. **Iteration 5:**
   - **Citation Array:** `[10, 8, 5, 4, 3]`
   - **Index (`i`):** 4
   - **Citation Count (`num`):** 3
   - **`i + 1`:** 5
   - **Condition (`num >= i + 1`):** `3 >= 5` → **False**
   - **Break the loop, final h-index is 4.**

This breakdown matches the earlier table, and the h-index is calculated to be **4**.

### Time Complexity:
- **O(n log n)** due to sorting the citations list.
