## Problem Statement

The problem "Two Sum" involves finding two numbers in an array that add up to a given target. You are given an array of integers `nums` and an integer `target`. Your task is to return the indices of the two numbers such that they add up to the target. It is guaranteed that each input would have exactly one solution, and you may not use the same element twice. The solution can be returned in any order.

### Function Signature

```python
def twoSum(nums, target):
    pass
```

### Input Parameters

- `nums`: A list of integers.
- `target`: An integer representing the target sum.

### Output

- A list of two integers representing the indices of the two numbers in the array that add up to the target.

### Example Inputs and Outputs

**Example 1:**

- **Input:** `nums = [2, 7, 11, 15]`, `target = 9`
- **Output:** `[0, 1]`
- **Explanation:** The numbers at indices 0 and 1 are 2 and 7, respectively, which add up to 9.

**Example 2:**

- **Input:** `nums = [3, 2, 4]`, `target = 6`
- **Output:** `[1, 2]`
- **Explanation:** The numbers at indices 1 and 2 are 2 and 4, respectively, which add up to 6.

### High-Level Approach

1. **Use a Hash Map for Lookup**: To efficiently find the complement of each number in the array, use a hash map (dictionary). The key will be the number itself, and the value will be its index in the array.

2. **Iterate Through the Array**: For each element in the array:
   - Calculate the complement, which is `target - nums[i]`.
   - Check if the complement exists in the hash map.
   - If it exists, return the indices of the current number and the complement.
   - If not, add the current number and its index to the hash map.

3. **Single Pass Solution**: The solution should ideally be achieved in a single pass through the array, making it efficient with O(n) time complexity.

### Example Implementation

```python
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]
```

In this implementation, the `twoSum` function uses a hash map to store the indices of the numbers as they are iterated over. It checks if the complement of the current number (i.e., the number needed to reach the target sum) is already in the hash map. If so, it returns the indices of the current number and the complement. If not, it adds the current number to the hash map. This ensures that the solution is found efficiently in O(n) time complexity.
