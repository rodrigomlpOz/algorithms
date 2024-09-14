### Problem Definition:
You are given an array of integers `nums` that represents a permutation of integers. The task is to find the **next lexicographical permutation** of the array. If no such permutation exists (i.e., the array is sorted in descending order), rearrange the array into the **lowest possible order** (i.e., sorted in ascending order). The solution must be done **in-place** and use **constant extra memory**.

### Function Definition:

```python
def nextPermutation(nums: List[int]) -> None:
    """
    Modifies the list nums in-place to its next lexicographical permutation.
    If no next permutation exists, rearranges nums into the smallest lexicographical order.
    """
    # Your code here
```

### High-Level Approach:
1. **Find the First Decreasing Element:**
   - Traverse the array from the end to find the first element `nums[i]` where `nums[i] < nums[i + 1]`. This element is the "first decreasing element."

2. **Find the Next Larger Element:**
   - After identifying `nums[i]`, find the smallest element larger than `nums[i]` in the right portion of the array (`nums[j]`).

3. **Swap Elements:**
   - Swap `nums[i]` with `nums[j]` to generate the next larger permutation.

4. **Reverse the Subarray:**
   - Reverse the subarray after index `i` (i.e., `nums[i + 1:]`) to ensure that the remaining portion is in the smallest possible order.

### Example Calls:

#### Example 1:
```python
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
```

#### Example 2:
```python
nums = [3, 2, 1]
nextPermutation(nums)
print(nums)  # Output: [1, 2, 3]
```

#### Example 3:
```python
nums = [1, 1, 5]
nextPermutation(nums)
print(nums)  # Output: [1, 5, 1]
```

### High-Level Flow:

1. **Identify the first pair of elements that break the descending order from the back.**
2. **Find the smallest element to the right of that pair that is larger than the identified element.**
3. **Swap those two elements.**
4. **Reverse the segment of the list that comes after the swapped element to get the next lexicographical permutation.**

This approach ensures that we find the next permutation in **O(n)** time with **O(1)** extra space.
