Certainly! Below is the revised problem description for converting an integer to a Roman numeral. This version replaces the traditional input/output examples with `print` statements that demonstrate function calls and their corresponding outputs.

---

## Problem: Integer to Roman Numeral Converter

### Description

Roman numerals are a numeral system originating from ancient Rome, used throughout Europe until the late Middle Ages. They are based on combinations of letters from the Latin alphabet: **I**, **V**, **X**, **L**, **C**, **D**, and **M**.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are typically written largest to smallest from left to right. However, to avoid four characters being repeated in succession, subtractive notation is used:

- **IV** (4) instead of **IIII**
- **IX** (9) instead of **VIIII**
- **XL** (40) instead of **XXXX**
- **XC** (90) instead of **LXXXX**
- **CD** (400) instead of **CCCC**
- **CM** (900) instead of **DCCCC**

Given an integer, convert it to its corresponding Roman numeral representation.

### Function Signature

```python
def int_to_roman(num: int) -> str:
    val = [
    1000, 900, 500, 400, 
    100, 90, 50, 40, 
    10, 9, 5, 4, 
    1
    ]
    syb = [
        "M", "CM", "D", "CD", 
        "C", "XC", "L", "XL", 
        "X", "IX", "V", "IV", 
        "I"
    ]
```

### Parameters

- `num` (int): An integer between 1 and 3999 inclusive.

### Returns

- `str`: The Roman numeral representation of the given integer.

### Constraints

- `1 <= num <= 3999`

### Examples

#### Example 1

```python
print(int_to_roman(3))  # Output: "III"
```
**Explanation**:  
3 is represented as three ones.

#### Example 2

```python
print(int_to_roman(4))  # Output: "IV"
```
**Explanation**:  
4 is represented as one before five.

#### Example 3

```python
print(int_to_roman(9))  # Output: "IX"
```
**Explanation**:  
9 is represented as one before ten.

#### Example 4

```python
print(int_to_roman(58))  # Output: "LVIII"
```
**Explanation**:  
L = 50, V = 5, III = 3.

#### Example 5

```python
print(int_to_roman(1994))  # Output: "MCMXCIV"
```
**Explanation**:  
M = 1000, CM = 900, XC = 90, IV = 4.

### Provided Implementation

Here's a Python function that converts an integer to a Roman numeral:

```python
def int_to_roman(num):
    val = [
        1000, 900, 500, 400, 
        100, 90, 50, 40, 
        10, 9, 5, 4, 
        1
    ]
    syb = [
        "M", "CM", "D", "CD", 
        "C", "XC", "L", "XL", 
        "X", "IX", "V", "IV", 
        "I"
    ]
    roman_num = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman_num += syb[i]
            num -= val[i]
    return roman_num

# Example usage:
print(int_to_roman(1994))  # Output: MCMXCIV
```

### Explanation of the Implementation

1. **Value and Symbol Arrays**:
   - `val`: A list of integer values in descending order, including those that require subtractive notation (e.g., 900, 400).
   - `syb`: A corresponding list of Roman numeral symbols for each value in `val`.

2. **Building the Roman Numeral**:
   - Initialize an empty string `roman_num` to store the resulting Roman numeral.
   - Iterate over each value in `val`:
     - While the current number `num` is greater than or equal to `val[i]`, append the corresponding symbol `syb[i]` to `roman_num` and subtract `val[i]` from `num`.
   - Continue this process until the entire number is converted.

3. **Example Walkthrough** (`num = 1994`):
   - 1994 >= 1000: Append "M", subtract 1000 → `roman_num = "M"`, `num = 994`
   - 994 >= 900: Append "CM", subtract 900 → `roman_num = "MCM"`, `num = 94`
   - 94 >= 90: Append "XC", subtract 90 → `roman_num = "MCMXC"`, `num = 4`
   - 4 >= 4: Append "IV", subtract 4 → `roman_num = "MCMXCIV"`, `num = 0`
   - Conversion complete: "MCMXCIV"

### Time and Space Complexity

- **Time Complexity**: O(1)
  - The maximum number of iterations is fixed since the input is constrained between 1 and 3999.
  
- **Space Complexity**: O(1)
  - The space used for the `val` and `syb` lists is constant, and the resulting `roman_num` string's length is bounded by a constant.

### Additional Notes

- This implementation efficiently handles all possible cases within the given constraints by leveraging the predefined value-symbol mappings.
- Subtractive notation is seamlessly integrated by including values like 900 (`"CM"`), 400 (`"CD"`), etc., in the `val` list.

---

Feel free to use this problem description for educational purposes, coding challenges, or any other relevant applications!
