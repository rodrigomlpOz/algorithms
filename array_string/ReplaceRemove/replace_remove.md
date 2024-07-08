### Problem Statement

You are given an array of characters, where each character is either 'a', 'b', or any other character. You need to perform two operations on this array:

1. Replace each 'a' with two 'd's.
2. Delete each entry containing a 'b'.

You need to modify the array in place and return the new length of the array after these operations.

### Function Signature

```python
def replace_and_remove(s: list[str]) -> int:
```

### High-Level Approach

1. **Forward Iteration: Remove 'b's and Count 'a's**
   - Traverse the array from the start.
   - Skip any 'b' by not copying it to the new position.
   - Count the number of 'a's encountered.

2. **Backward Iteration: Replace 'a's with 'dd's**
   - Traverse the modified array from the end.
   - Start replacing 'a's with two 'd's from the back to avoid overwriting.
   - Move non-'a' characters to their new positions.

3. **Return the New Length**
   - The length of the array after performing the above operations will be returned.

### Detailed Steps

1. **Forward Iteration:**
   - Initialize `write_idx` to 0 (to keep track of where to write the next character).
   - Initialize `a_count` to 0 (to count the number of 'a's).
   - Iterate through the array:
     - If the current character is not 'b', write it to the `write_idx` position and increment `write_idx`.
     - If the current character is 'a', increment `a_count`.

2. **Backward Iteration:**
   - Adjust `write_idx` to the new end of the array after replacing 'a's with 'dd's.
   - Traverse the array backward from the last valid character:
     - If the current character is 'a', write 'dd' in the correct positions and adjust `write_idx`.
     - If the current character is not 'a', move it to the `write_idx` position.

3. **Return the Length:**
   - The final length of the array will be the adjusted `write_idx` plus one.

### Example

Given the input array `['a', 'c', 'd', 'b', 'b', 'c', 'a']`:
- After the forward iteration: `['a', 'c', 'd', 'c', 'a', '_', '_']` with `a_count = 2`.
- After the backward iteration: `['d', 'd', 'c', 'd', 'c', 'd', 'd']`.
- The new length is 7.

