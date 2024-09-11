### Problem Definition:
The **Maximum Product Subarray** problem asks you to find the contiguous subarray within an array (containing at least one number) that has the largest product.

### Function Definition:
```python
def maxProduct(nums: list[int]) -> int:
```

- **Input**: A list of integers `nums` where `nums[i]` can be positive, negative, or zero.
- **Output**: The maximum product of a contiguous subarray.

### Example Calls:
```python
# Example 1
print(maxProduct([2, 3, -2, 4]))  # Output: 6 (subarray: [2, 3])

# Example 2
print(maxProduct([-2, 0, -1]))  # Output: 0 (subarray: [0])

# Example 3
print(maxProduct([-2, 3, -4]))  # Output: 24 (subarray: [-2, 3, -4])

# Example 4
print(maxProduct([0, 2]))  # Output: 2 (subarray: [2])
```

### High-Level Solution:
The key challenge with finding the maximum product subarray is handling both negative and positive numbers. A negative number can turn a small product into a large one, and vice versa. Therefore, at each step, we need to keep track of both the maximum product and the minimum product up to the current number.

1. **Initialize `max_product`, `min_product`, and `result`** with the first element of the array. These variables will help in calculating the maximum and minimum product subarrays up to the current index.
  
2. **Iterate through the array starting from the second element**. For each element:
   - If the current number is negative, swap `max_product` and `min_product` because multiplying by a negative reverses the roles of the maximum and minimum.
   
   - Update `max_product` to be the maximum of the current number itself or the product of the current number with the previous `max_product`.
   
   - Similarly, update `min_product` to be the minimum of the current number itself or the product of the current number with the previous `min_product`.

3. **Update `result`** to be the maximum of itself and `max_product`, which holds the largest product found so far.

4. After the loop finishes, return the value of `result`.

### Final Solution Code:

```python
def maxProduct(nums: list[int]) -> int:
    if not nums:
        return 0

    # Step 1: Initialize max_product, min_product, and result with the first element
    max_product = min_product = result = nums[0]

    # Step 2: Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current number is negative, swap max_product and min_product
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        # Step 3: Update max_product and min_product
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        # Step 4: Update the result to the maximum product found so far
        result = max(result, max_product)

    return result
```

### Time Complexity:
- **O(n)** where `n` is the length of the input array, since we traverse the array once.

### Space Complexity:
- **O(1)** since we only use a constant amount of space for the variables `max_product`, `min_product`, and `result`.
