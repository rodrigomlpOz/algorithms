### Problem Statement:
Given an array of integers `citations`, where `citations[i]` is the number of citations a researcher received for their ith paper, return the researcher's **h-index**. 

The **h-index** is defined as the maximum value `h` such that the researcher has published at least `h` papers that have each been cited at least `h` times.

### Function Definition:
```python
class Solution:
    def hIndex(self, citations: list[int]) -> int:
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

### Time Complexity:
- **O(n log n)** due to sorting the citations list.