### Problem Statement:
You are given an array `A` that consists of `k` alternating increasing and decreasing subarrays. Your task is to sort the entire array efficiently by leveraging the fact that each subarray is already sorted, either in increasing or decreasing order.

### Example:
**Input:**  
```
A = [1, 3, 5, 4, 2, 6, 8, 7]
```
This input has 4 subarrays:
- Subarray 1 (increasing): `[1, 3, 5]`
- Subarray 2 (decreasing): `[4, 2]`
- Subarray 3 (increasing): `[6, 8]`
- Subarray 4 (decreasing): `[7]`

**Output:**  
```
[1, 2, 3, 4, 5, 6, 7, 8]
```
The goal is to sort the array into one fully sorted array.

---

### Function Definition:

```python
def sort_k_increasing_decreasing_array(A):
    """
    Sorts an array consisting of k increasing and decreasing subarrays.

    Args:
    A: List[int] - The input array.

    Returns:
    List[int] - A fully sorted array.
    """
    pass  # Implementation will go here
```

---

### Function Calls:

```python
# Test Case 1
A = [1, 3, 5, 4, 2, 6, 8, 7]
print(sort_k_increasing_decreasing_array(A))  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8]

# Test Case 2
A = [9, 7, 6, 4, 1, 10, 11, 12]
print(sort_k_increasing_decreasing_array(A))  # Expected output: [1, 4, 6, 7, 9, 10, 11, 12]
```

---

### High-Level Solution:

1. **Step 1: Decomposition into Sorted Subarrays**
   - The first step is to decompose the given array `A` into a series of sorted subarrays. We can detect transitions between increasing and decreasing sequences as we iterate through the array.
   - When a transition is detected, we add the current subarray to a list:
     - If the subarray is increasing, it is added as is.
     - If the subarray is decreasing, it is reversed before being added to ensure it is sorted in increasing order.

2. **Step 2: Merging the Sorted Subarrays**
   - Once the array is decomposed into `k` sorted subarrays, we merge them into a single fully sorted array.
   - Merging can be done efficiently using a min-heap (priority queue), which allows us to always extract the smallest element from the available sorted subarrays.

3. **Final Output:**
   - The fully merged and sorted array is the final output, combining all the sorted subarrays into one.

### Process Overview:
1. **Decompose the Array:**
   - Loop through the array and break it into sorted subarrays (either increasing or decreasing).
   - Reverse the decreasing subarrays to make them increasing.

2. **Merge the Subarrays:**
   - Merge all the sorted subarrays using a heap to efficiently combine them into one sorted array.

### Time Complexity:
- **Decomposition:** Takes **O(n)** time, where `n` is the length of the array.
- **Merging:** Takes **O(n log k)** time, where `k` is the number of subarrays (due to the use of a heap).

Thus, the overall time complexity is **O(n log k)**.

Let me know if you'd like further details or explanations!
