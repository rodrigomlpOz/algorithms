### Problem Definition:

The **Majority Element** in an array is the element that appears more than `n // 2` times, where `n` is the length of the array.

You are given an array of integers `nums`. Your task is to return the majority element. It is guaranteed that a majority element always exists in the array.

### Function Definition:

```python
def majorityElement(nums: List[int]) -> int:
    """
    Finds the majority element in the array, which appears more than n // 2 times.
    
    :param nums: List[int] - The input list of integers
    :return: int - The majority element
    """
    # Your code here
```

### High-Level Approach:

We can solve the problem efficiently using **Boyer-Moore Voting Algorithm**, which runs in `O(n)` time and uses `O(1)` space. This algorithm works by maintaining a candidate for the majority element and a count, adjusting them as we iterate through the array.

### Approach:

1. **Boyer-Moore Voting Algorithm**:
   - **Candidate Selection:** We maintain a candidate for the majority element and a count. As we iterate through the array:
     - If the count is `0`, we select the current element as the new candidate.
     - If the current element is the same as the candidate, we increment the count.
     - If the current element is different from the candidate, we decrement the count.
   - By the end of the iteration, the candidate will be the majority element because it appears more than `n // 2` times.

### Code Implementation:

```python
def majorityElement(nums: List[int]) -> int:
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate
```

### Explanation:

1. **Candidate Selection:**
   - We start with `candidate = None` and `count = 0`.
   - As we iterate through `nums`:
     - If `count` is `0`, we set `candidate = num`.
     - If `num == candidate`, we increment `count`.
     - If `num != candidate`, we decrement `count`.

2. **Return the Candidate:**
   - The final value of `candidate` will be the majority element because it is guaranteed that such an element exists in the array.

### Example Calls:

#### Example 1:
```python
nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3
```

#### Example 2:
```python
nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))  # Output: 2
```

### Time and Space Complexity:

- **Time Complexity:** `O(n)`, where `n` is the length of the array. We iterate through the array once.
- **Space Complexity:** `O(1)`, as we only use two extra variables (`candidate` and `count`).

This approach efficiently finds the majority element using a single pass through the array with constant space.
