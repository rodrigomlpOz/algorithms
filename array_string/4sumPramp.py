### Problem Statement: Find Array Quadruplet

Given an unsorted array of integers `arr` and a target sum `s`, write a function `findArrayQuadruplet` that finds four numbers (quadruplet) in `arr` that sum up to `s`. Your function should return an array of these numbers in ascending order. If such a quadruplet doesn’t exist, return an empty array.

#### Function Signature
```python
def findArrayQuadruplet(arr: List[int], s: int) -> List[int]:
```

#### Example

**Input:**
```plaintext
arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
```

**Output:**
```plaintext
[0, 4, 7, 9]
```

**Explanation:**
The ordered quadruplet (0, 4, 7, 9) sums up to 20. Notice that there are other quadruplets that also sum up to 20, such as (7, 9, 1, 3) and (2, 4, 9, 5), but you are required to return just one quadruplet in ascending order.

### Constraints:
1. The input array `arr` will have at least four elements.
2. Elements in `arr` can be both positive and negative integers.
3. If multiple quadruplets sum to `s`, any one of them in ascending order is acceptable.





















#Solution 

### Approach:
To solve this problem efficiently, consider the following approach:
1. Sort the array.
2. Use a nested loop to fix the first two elements.
3. Use a two-pointer technique to find the remaining two elements that sum to the required value.

### Example Code:
```python
from typing import List

def findArrayQuadruplet(arr: List[int], s: int) -> List[int]:
    n = len(arr)
    if n < 4:
        return []

    arr.sort()
    
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            
            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if current_sum == s:
                    return [arr[i], arr[j], arr[left], arr[right]]
                elif current_sum < s:
                    left += 1
                else:
                    right -= 1

    return []
```

This function first sorts the array and then uses two nested loops to fix the first two elements. It then uses the two-pointer technique to find the other two elements that sum up to the target value `s`. The function returns the quadruplet in ascending order if found, otherwise, it returns an empty array.
