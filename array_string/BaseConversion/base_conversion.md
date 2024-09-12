### Problem Statement: Convert Number Between Bases

Given a number represented in a base \( b_1 \) and a target base \( b_2 \), write a function to convert the number from base \( b_1 \) to base \( b_2 \). You can assume that the input number is a valid number in base \( b_1 \).

#### Function Signature

**Python:**

```python
def base_conversion(num: str, b1: int, b2: int) -> str:
    # Function implementation
```

#### Example

Input:

```python
num = "1011"
b1 = 2
b2 = 10
```

Output:

```python
"11"
```

Explanation: The number "1011" in base 2 is equivalent to "11" in base 10.

#### Constraints:

1. The input number will be a valid number in the given base \( b_1 \).
2. \( 2 \leq b_1, b_2 \leq 36 \).
3. The digits in the number can include 0-9 and A-Z, where A represents 10, B represents 11, ..., and Z represents 35.

### Example Function Calls

```python
# Example 1: Binary to Decimal
result = base_conversion('1011', 2, 10)
print(f"base_conversion('1011', 2, 10) = {result}")  # Output: "11"

# Example 2: Decimal to Binary
result = base_conversion('11', 10, 2)
print(f"base_conversion('11', 10, 2) = {result}")  # Output: "1011"

# Example 3: Hexadecimal to Decimal
result = base_conversion('1A', 16, 10)
print(f"base_conversion('1A', 16, 10) = {result}")  # Output: "26"

# Example 4: Decimal to Hexadecimal
result = base_conversion('26', 10, 16)
print(f"base_conversion('26', 10, 16) = {result}")  # Output: "1A"

# Example 5: Base 5 to Base 3
result = base_conversion('132', 5, 3)
print(f"base_conversion('132', 5, 3) = {result}")  # Output: "1102"

# Example 6: Negative Number in Base 10 to Binary
result = base_conversion('-11', 10, 2)
print(f"base_conversion('-11', 10, 2) = {result}")  # Output: "-1011"

# Example 7: Base 36 to Decimal
result = base_conversion('Z', 36, 10)
print(f"base_conversion('Z', 36, 10) = {result}")  # Output: "35"

# Example 8: Decimal to Base 36
result = base_conversion('35', 10, 36)
print(f"base_conversion('35', 10, 36) = {result}")  # Output: "Z"

# Example 9: Base 8 to Base 16
result = base_conversion('17', 8, 16)
print(f"base_conversion('17', 8, 16) = {result}")  # Output: "F"

# Example 10: Large Number from Base 10 to Base 2
result = base_conversion('123456789', 10, 2)
print(f"base_conversion('123456789', 10, 2) = {result}")  # Output: "111010110111100110100010101"
```

### High Level Solution

1. **Convert to Decimal**: The first step is to convert the given number from its base \( b_1 \) to a base 10 integer. This can be done by iterating over each digit of the number, multiplying it by the base raised to the appropriate power, and summing the results.

2. **Convert to Target Base**: Once the number is in base 10, convert it to the target base \( b_2 \). This involves repeatedly dividing the number by \( b_2 \) and recording the remainders. The remainders represent the digits of the number in the target base, and they should be collected in reverse order.

3. **Handle Negative Numbers**: If the original number is negative, ensure that the final result also reflects this by adding a '-' sign.

4. **Edge Cases**: Consider edge cases such as zero, and ensure that the implementation handles bases up to 36, which includes digits 0-9 and letters A-Z.
5. 
Here's a short example you can include in your documentation to explain the usage of `%` in base conversion:

---

### Example: Using Modulo for Base Conversion

The modulo operation (`%`) is used in base conversion to extract the digits of a number when converting from a decimal (base 10) to another base. Each `%` operation provides the next least significant digit in the target base.

#### Example: Convert `19` from decimal (base 10) to binary (base 2)

1. **Start with 19**  
   `19 % 2 = 1` → The rightmost binary digit is `1`.  
   Divide: `19 // 2 = 9`.

2. **Next digit**  
   `9 % 2 = 1` → The next binary digit is `1`.  
   Divide: `9 // 2 = 4`.

3. **Continue**  
   `4 % 2 = 0` → The next binary digit is `0`.  
   Divide: `4 // 2 = 2`.

4. **Next digit**  
   `2 % 2 = 0` → The next binary digit is `0`.  
   Divide: `2 // 2 = 1`.

5. **Final digit**  
   `1 % 2 = 1` → The next binary digit is `1`.  
   Divide: `1 // 2 = 0`.

The binary representation of `19` is the reverse of the digits collected: **`10011`**.

---

This example shows how `%` helps in extracting digits during base conversion.
