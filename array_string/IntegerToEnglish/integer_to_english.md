### Problem Definition:

You are given a non-negative integer `num`. The task is to convert this number into its English words representation.

### Function Definition:

```python
def numberToWords(num: int) -> str:
    """
    Convert a non-negative integer to its English words representation.
    
    :param num: int - A non-negative integer
    :return: str - English words representation of the integer
    """
    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

```
### Approach:

1. **Edge Case:** If `num` is 0, return `"Zero"`.
2. **Define Word Representations:**
   - Create mappings for numbers from 1 to 19 (as these have unique names), tens (like twenty, thirty), and large numbers (thousand, million, billion).
3. **Recursive Processing:**
   - For each group of three digits (hundreds, thousands, millions, etc.), recursively convert it into words.
4. **Base Case Handling:**
   - Recursively handle groups by dividing the number by powers of 1000. For each group, form the English representation by combining the hundreds, tens, and ones.

### Code Implementation:

```python
class Solution:
    
```

### Explanation:

1. **Initial Check:** If `num` is `0`, return `"Zero"`.
2. **Helper Function:** The `helper` function converts numbers smaller than 1000 into their English word equivalents.
   - If the number is less than 20, return the corresponding word from the `below_20` list.
   - If the number is less than 100, return the corresponding tens word and recursively call `helper` for the ones digit.
   - If the number is 100 or more, return the hundreds word and recursively call `helper` for the rest of the number.
3. **Main Loop:** The main loop processes the number in chunks of three digits (i.e., handling thousands, millions, and billions) by dividing the number by 1000 in each iteration. Each group of digits is converted to words using the `helper` function and appended to the result with the appropriate thousand/million/billion unit.
4. **Return the Final Result:** After processing all the digits, return the resulting string without leading or trailing spaces.

### Example Calls:

#### Example 1:
```python
num = 123
sol = Solution()
print(sol.numberToWords(num))  # Output: "One Hundred Twenty Three"
```

#### Example 2:
```python
num = 12345
sol = Solution()
print(sol.numberToWords(num))  # Output: "Twelve Thousand Three Hundred Forty Five"
```

#### Example 3:
```python
num = 1234567
sol = Solution()
print(sol.numberToWords(num))  # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

### Time and Space Complexity:

- **Time Complexity:** `O(n)` where `n` is the number of digits in the input number. We process each group of three digits once.
- **Space Complexity:** `O(1)` (constant space) since we only use a few lists for word mappings and a recursive function.

This approach efficiently converts any non-negative integer into its English words representation.
