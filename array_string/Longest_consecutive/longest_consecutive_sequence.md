### Problem Statement:
Given an array of integers `nums`, return the length of the longest consecutive sequence of elements. A consecutive sequence is a sequence in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in **O(n)** time.

### Function Definition:
```python
def longestConsecutive(nums: list[int]) -> int:
# Function to return the length of the longest consecutive sequence
   pass
```

### Example 1:
```python
nums = [2, 20, 4, 10, 3, 4, 5]
# The longest consecutive sequence is [2, 3, 4, 5]
# Output: 4
```

### Example 2:
```python
nums = [0, 3, 2, 5, 4, 6, 1, 1]
# The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6]
# Output: 7
```

### Constraints:
- `0 <= nums.length <= 1000`
- `-10^9 <= nums[i] <= 10^9`

### High-Level Description:
1. **Objective**: Find the length of the longest sequence of consecutive integers in the array.
2. **Approach**:
   - Convert the list into a **set** to remove duplicates and allow O(1) lookups.
   - Iterate through the set and, for each number that could be the start of a sequence (i.e., the number has no predecessor in the set), compute the length of the sequence.
   - Track the maximum sequence length encountered.
3. **Efficiency**:
   - Time Complexity: **O(n)**, where `n` is the number of elements in `nums`. Each element is processed once due to the set and subsequent checks.
   - Space Complexity: **O(n)**, for storing the elements in the set.
