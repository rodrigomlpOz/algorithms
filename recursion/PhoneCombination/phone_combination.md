## Problem Statement

Given a string containing digits from 2 to 9 inclusive, return all possible letter combinations that the number could represent. Each digit corresponds to a set of letters as on the telephone buttons. The mapping is given as follows:

- 2 -> "abc"
- 3 -> "def"
- 4 -> "ghi"
- 5 -> "jkl"
- 6 -> "mno"
- 7 -> "pqrs"
- 8 -> "tuv"
- 9 -> "wxyz"

## Function Signature

```python
def letterCombinations(self, digits):
    pass
```

### Input Parameters

- `digits`: A string containing digits from '2' to '9'.

### Output

- A list of strings, where each string represents a possible letter combination.

### Example Inputs and Outputs

**Example 1:**

- **Input:** `digits = "23"`
- **Output:** `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

**Example 2:**

- **Input:** `digits = ""`
- **Output:** `[]`

## High-Level Approach

1. **Mapping Digits to Letters**: Use a dictionary to map each digit to its corresponding letters. For example, '2' maps to "abc", '3' to "def", and so on.

2. **Backtracking**: Use a backtracking approach to generate all possible combinations:
   - **Base Case**: If the current temporary combination (`temp`) has a length equal to the input `digits`, add it to the result list.
   - **Recursive Case**: For each digit in the input string, append each corresponding letter to the temporary combination, recurse for the next digit, and backtrack by removing the letter (undoing the choice).

3. **Edge Case**: If the input `digits` is an empty string, immediately return an empty list since there are no combinations to generate.

