### Problem Description (Jump Game II):

You are given a 0-indexed array of integers `nums` of length `n`. Each element in `nums[i]` represents the maximum number of steps you can jump forward from that position. You are initially at the first index (position 0), and your goal is to reach the last index (`nums[n-1]`) with the **minimum number of jumps**.

- The test cases are guaranteed such that you can always reach the last index.

### Example 1:

```python
Input: nums = [2, 3, 1, 1, 4]
Output: 2
Explanation: 
- Jump 1 step from index 0 to index 1, and
- Jump 3 steps from index 1 to the last index.
```

### Example 2:

```python
Input: nums = [2, 3, 0, 1, 4]
Output: 2
Explanation: 
- Jump 1 step from index 0 to index 1, and
- Jump 3 steps from index 1 to the last index.
```

---

### Function Definition:

```python
def jump(nums: list[int]) -> int:
    pass
```

### Function Calls:

```python
print(jump([2, 3, 1, 1, 4]))  # Expected Output: 2
print(jump([2, 3, 0, 1, 4]))  # Expected Output: 2
```

---

### High-Level Solution:

This problem can be solved efficiently using a **greedy approach**. The idea is to keep track of the **current jump range** and update it as you go through the array.

#### Steps:

1. **Greedy Choice**:
   - At every index `i`, track the farthest position you can jump to using the current jump range.
   - Keep expanding the range and increment the jump count only when you exceed the current range.

2. **Track Important Variables**:
   - `jumps`: This tracks the total number of jumps taken.
   - `current_end`: This tracks the farthest index that can be reached with the current jump.
   - `farthest`: This tracks the farthest index that can be reached from any position within the current range.

3. **Iterate Through the Array**:
   - For each index `i`, update the farthest position that can be reached.
   - If `i` reaches `current_end`, increment the jump count and update `current_end` to the farthest index.

4. **Return the Result**:
   - Once you reach or exceed the last index, return the total number of jumps.

---

### Code Implementation:

```python
def jump(nums: list[int]) -> int:
    jumps = 0         # Count the number of jumps
    current_end = 0    # Farthest point we can reach with the current jump
    farthest = 0       # Farthest point we can reach overall
    
    for i in range(len(nums) - 1):
        # Update the farthest point we can reach from this index
        farthest = max(farthest, i + nums[i])
        
        # If we reach the end of the current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest
        
        # If we've already reached or exceeded the last index
        if current_end >= len(nums) - 1:
            break
    
    return jumps
```

---

### Walkthrough:

Let’s walk through an example to see how this solution works.

#### Example: `nums = [2, 3, 1, 1, 4]`

- **Initial State**:
  - `jumps = 0`: No jumps made yet.
  - `current_end = 0`: We are currently at the first index.
  - `farthest = 0`: The farthest point we can reach from the first index is 0.

- **Iteration 1 (i = 0)**:
  - From index 0, we can jump up to `2` steps forward, so the farthest index we can reach is `farthest = max(0, 0 + 2) = 2`.
  - Since `i == current_end`, we make a jump: `jumps = 1`.
  - Update `current_end = farthest = 2`.

- **Iteration 2 (i = 1)**:
  - From index 1, we can jump up to `3` steps forward, so the farthest index we can reach is `farthest = max(2, 1 + 3) = 4`.
  - We haven’t reached `current_end` yet, so no jump is made here.

- **Iteration 3 (i = 2)**:
  - From index 2, we can jump only `1` step forward, so `farthest` remains `4` (since it's already greater).
  - Now, `i == current_end`, so we make another jump: `jumps = 2`.
  - Update `current_end = farthest = 4`.

- **Final Check**:
  - At this point, `current_end >= len(nums) - 1`, which means we’ve reached the last index.
  - The total number of jumps is `2`.

### Result:

For `nums = [2, 3, 1, 1, 4]`, the minimum number of jumps is **2**.

---

### Time and Space Complexity:

- **Time Complexity**: \(O(n)\), where \(n\) is the number of elements in the array. We only traverse the array once.
- **Space Complexity**: \(O(1)\), as we only use a constant amount of extra space (`jumps`, `current_end`, `farthest`).