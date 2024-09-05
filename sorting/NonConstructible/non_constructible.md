### Problem Definition

Given a list of positive integers representing coin denominations, find the smallest amount of money that **cannot** be formed using these denominations. The coins can be used multiple times, and the goal is to determine the smallest value that cannot be constructed by summing any combination of the given denominations.

### Function Definition

```python
def smallest_nonconstructible_value(A):
    """
    Finds the smallest non-constructible value that cannot be formed using 
    any combination of the integers in the list A.
    
    Args:
    A : list
        A list of positive integers representing coin denominations.
        
    Returns:
    int : The smallest non-constructible value.
    """
```

### High-Level Steps

1. **Sorting the List**: 
   Sort the list of coin denominations to process them in increasing order. This ensures we evaluate whether all smaller values can be constructed before handling larger coins.

2. **Tracking Constructible Values**: 
   Initialize a variable `max_constructible_value` to track the maximum value that can be constructed using the coins encountered so far.

3. **Iterating Through Coins**: 
   Iterate over each coin in the sorted list:
   - If the current coin is greater than `max_constructible_value + 1`, then we have found a gap, meaning there is a value that cannot be constructed using the previous coins.
   - If the coin is smaller than or equal to `max_constructible_value + 1`, add it to `max_constructible_value` to update the range of constructible values.

4. **Return the Result**: 
   After the loop, return the smallest value that cannot be constructed, which is `max_constructible_value + 1`.

### Example

```python
coins = [1, 2, 2, 5]
result = smallest_nonconstructible_value(coins)
print(result)  # Output: 11
```

In this example, the smallest value that cannot be constructed using the given coin denominations is 11.
