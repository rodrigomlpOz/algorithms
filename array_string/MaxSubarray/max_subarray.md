### Problem: Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#### Function Signature:
```python
def maxSubArray(nums: List[int]) -> int
```

#### Input:
- `nums` (List[int]): A list of integers representing the array.

#### Output:
- (int): The sum of the contiguous subarray with the largest sum.

#### Example:
```python
assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert maxSubArray([1]) == 1
assert maxSubArray([5,4,-1,7,8]) == 23
```

### High-Level Approach:
1. **Initialize Variables**: Start by initializing two variables: `current_subarray` and `max_subarray` with the first element of the array. These variables will help keep track of the sum of the current subarray being considered and the maximum subarray sum found so far, respectively.
2. **Iterate Through Array**: Iterate through the array starting from the second element.
3. **Update Current Subarray**: For each element, decide whether to add the element to the current subarray (i.e., continue the current subarray) or start a new subarray with the current element. This is determined by comparing the element itself with the sum of the element and the current subarray.
4. **Update Maximum Subarray**: Update `max_subarray` to be the maximum of itself and the `current_subarray`. This ensures that `max_subarray` always holds the largest sum found so far.
5. **Return Result**: After iterating through the array, `max_subarray` will contain the maximum sum of any contiguous subarray in the input array.

This approach ensures that the problem is solved in linear time, making it efficient even for large input arrays.
