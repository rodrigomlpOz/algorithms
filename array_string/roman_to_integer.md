### Problem Statement:
Roman numerals are represented by seven different symbols: `I, V, X, L, C, D, M`, where each symbol represents a specific integer value. The challenge is to convert a given Roman numeral string into an integer.

### Roman Numeral Values:
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Certain numerals are formed by placing smaller values before larger ones to indicate subtraction:
- `IV` = 4 (I before V)
- `IX` = 9 (I before X)
- `XL` = 40 (X before L)
- `XC` = 90 (X before C)
- `CD` = 400 (C before D)
- `CM` = 900 (C before M)

### Function Definition:
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # Function to convert Roman numeral string to an integer
```

### Approach:
1. **Map Roman Symbols to Values**: Create a dictionary to store the integer values for each Roman numeral symbol.
2. **Traverse the String**:
   - Check the value of each character.
   - If a smaller numeral appears before a larger one, subtract the smaller from the larger.
   - Otherwise, just add the value of the numeral.
3. **Return the Total Sum**.

### Code:

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to their respective integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize total to 0
        total = 0
        
        # Traverse the Roman numeral string
        for i in range(len(s)):
            # If the current numeral is smaller than the next one, subtract it
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, add the current numeral's value
                total += roman_map[s[i]]
        
        return total
```

### Explanation of the Code:
1. **Dictionary**: A dictionary `roman_map` is used to map each Roman numeral symbol to its corresponding integer value.
2. **Looping**: The loop iterates over the string `s`. If the current numeral is smaller than the next numeral (e.g., `I` before `V`), the current numeral's value is subtracted. Otherwise, it is added to the total.
3. **Final Sum**: After the loop finishes, the `total` contains the integer value of the Roman numeral string.

### Example Walkthrough:

#### Example 1:
```python
Input: s = "III"
Explanation: III = 1 + 1 + 1 = 3.
Output: 3
```

#### Example 2:
```python
Input: s = "LVIII"
Explanation: L = 50, V = 5, III = 3.
Output: 58
```

#### Example 3:
```python
Input: s = "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90, IV = 4.
Output: 1994
```

### Time and Space Complexity:
- **Time Complexity**: O(n), where `n` is the length of the string. Each character is processed once.
- **Space Complexity**: O(1), since the space used for the dictionary and the integer result is constant.

This approach efficiently converts Roman numerals to integers in linear time.
