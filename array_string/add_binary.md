### Problem Definition:

You are given two binary strings `a` and `b`. The task is to return their sum, also as a binary string. The input strings contain only the characters `'0'` or `'1'` and do not have any leading zeros, except in the case where the input is `"0"`.

### Function Definition:

```python
def addBinary(a: str, b: str) -> str:
    """
    Given two binary strings a and b, returns their sum as a binary string.
    """
    # Your code here
```

### High-Level Approach:

1. **Initialize Variables:**
   - Start with two pointers (`i` and `j`) at the end of each string, representing the current bit being processed from strings `a` and `b`.
   - Use a `carry` variable to track the carry-over during addition.

2. **Process from Right to Left:**
   - Iterate through both strings from the rightmost bit to the leftmost bit (similar to how addition is done by hand).
   - For each step, calculate the sum of the current bits (including any carry from the previous step).
   - Add the result to the final binary string and update the carry.

3. **Handle Remaining Carry:**
   - After processing all the bits, if there's any leftover carry, add it to the result.

4. **Return the Result:**
   - Since we build the result string from the least significant bit to the most significant bit, reverse the result before returning.

### Code Implementation:

```python
def addBinary(a: str, b: str) -> str:
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    # Process both strings from right to left
    while i >= 0 or j >= 0 or carry:
        # Get the current bit from both strings
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        
        # Sum the bits and the carry
        total = bit_a + bit_b + carry
        
        # Calculate the result bit and carry
        result_bit = total % 2
        carry = total // 2
        
        # Append the result bit to the result list
        result.append(str(result_bit))
        
        # Move the pointers
        i -= 1
        j -= 1
    
    # Since we are appending bits from right to left, reverse the result
    return ''.join(result[::-1])
```

### Example Calls:

#### Example 1:
```python
a = "11"
b = "1"
print(addBinary(a, b))  # Output: "100"
```

#### Example 2:
```python
a = "1010"
b = "1011"
print(addBinary(a, b))  # Output: "10101"
```

### High-Level Flow:

1. **Initialize pointers and carry** — Start from the least significant bit (rightmost) of both strings, and maintain a carry for each step of the addition.
2. **Bitwise addition** — Add corresponding bits from both strings, including the carry.
3. **Result construction** — Build the result bit-by-bit, and handle any remaining carry.
4. **Return the final binary sum** — Reverse the result string to return the correct binary sum.

### Time and Space Complexity:

- **Time Complexity:** `O(max(len(a), len(b)))` — We process each bit of both strings once.
- **Space Complexity:** `O(max(len(a), len(b)))` — The space required for the result string.
