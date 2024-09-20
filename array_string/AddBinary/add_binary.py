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
    return ''.join(reversed(result))


a = "11"
b = "1"
print(addBinary(a, b))  # Output: "100"

#### Example 2:
a = "1010"
b = "1011"
print(addBinary(a, b))  # Output: "10101"