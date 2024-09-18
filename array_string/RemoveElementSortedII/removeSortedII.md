Certainly! Here's a concise overview of **LeetCode Problem 80: Remove Duplicates from Sorted Array II** including the problem statement, function definition, example function calls, and a high-level solution.

---

### **Problem Statement**

Given a **sorted** integer array `nums`, remove duplicates **in-place** such that each unique element appears **at most twice**. Return the new length `k` of the array after removal. The relative order of elements should remain the same. You must achieve this with **O(1)** extra memory.

**Example:**
```plaintext
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
```

---

### **Function Definition**

```python
def removeDuplicates(nums: List[int]) -> int:
    # Your implementation here
```

---

### **Example Function Calls**

```python
# Example 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 5, [1, 1, 2, 2, 3]

# Example 2
nums2 = [0,0,1,1,1,1,2,3,3]
k2 = removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 7, [0, 0, 1, 1, 2, 3, 3]
```

---

### **High-Level Solution**

- **Two-Pointer Approach**:
  - **Write Pointer (`write`)**: Indicates the position to insert the next valid element. Initialize to `2` since the first two elements are always allowed.
  - **Iterate** through the array starting from the third element (`index 2`).
  - **For each element `nums[i]`**, compare it with `nums[write - 2]`:
    - **If different**, it's allowed. Assign `nums[write] = nums[i]` and increment `write`.
    - **If same**, skip the element to avoid exceeding the duplicate limit.
- **Result**: The `write` pointer will represent the new length `k`, with the first `k` elements of `nums` containing the desired result.

**Visualization:**
```plaintext
Initial: [1,1,1,2,2,3]
Process:
- Keep first two '1's.
- Skip the third '1'.
- Keep two '2's.
- Keep '3'.
Final: [1,1,2,2,3], k = 5
```

---

This approach ensures that each unique element appears at most twice while maintaining the array's sorted order, all achieved with a single pass and constant extra space.