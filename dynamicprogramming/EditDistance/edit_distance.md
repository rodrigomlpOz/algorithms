### Problem Statement (Edit Distance):
The **Edit Distance** (also known as **Levenshtein Distance**) between two strings is the minimum number of operations required to convert one string into the other. The allowed operations are:
1. **Insertion**: Insert a character.
2. **Deletion**: Delete a character.
3. **Substitution**: Replace one character with another.

The goal is to compute the minimum number of these operations needed to transform one string into another.

### Function Definition:
```python
def editDistance(str1, str2, m, n):
    """
    A function to calculate the minimum edit distance between two strings.

    Args:
    str1 : str : The first string.
    str2 : str : The second string.
    m : int : The length of the first string.
    n : int : The length of the second string.

    Returns:
    int : The minimum number of edit operations required to convert str1 to str2.
    """
    pass  # Logic will be implemented here
```

### Function Calls:
```python
# Example function calls for testing the editDistance function

str1 = "kitten"
str2 = "sitting"
m = len(str1)
n = len(str2)
print(editDistance(str1, str2, m, n))  # Expected output: 3

str1 = "horse"
str2 = "ros"
m = len(str1)
n = len(str2)
print(editDistance(str1, str2, m, n))  # Expected output: 3
```

### High-Level Solution:

1. **Objective:**
   The goal is to convert one string into another with the minimum number of operations (insertion, deletion, substitution). The challenge is to determine the sequence of operations that minimizes the number of changes.

2. **Base Case:**
   - If either string is empty, the only possible solution is to insert or delete all the characters of the other string. For example:
     - `editDistance("", "abc") = 3` (Insert all 3 characters).
     - `editDistance("abc", "") = 3` (Delete all 3 characters).

3. **Recursive Case:**
   For each character in the strings `str1` and `str2`, you have three possible choices:
   - **Insertion**: Insert a character in `str1` to match the next character in `str2`.
   - **Deletion**: Delete a character from `str1`.
   - **Substitution**: Replace the current character in `str1` with the corresponding character in `str2`.

   The recursive relation is:
   \[
   \text{editDistance}(str1, str2, m, n) = \min \left(
       \begin{array}{c}
       \text{editDistance}(str1, str2, m, n-1) + 1 \quad \text{(Insertion)} \\
       \text{editDistance}(str1, str2, m-1, n) + 1 \quad \text{(Deletion)} \\
       \text{editDistance}(str1, str2, m-1, n-1) + \text{cost} \quad \text{(Substitution)}
       \end{array}
   \right)
   \]
   Where the `cost` of substitution is `0` if the characters are the same, or `1` if they are different.

4. **Dynamic Programming Table:**
   - Create a DP table where `dp[i][j]` represents the minimum edit distance between the first `i` characters of `str1` and the first `j` characters of `str2`.
   - Fill the table using the recursive relation by considering all operations (insertion, deletion, substitution) at each step.
   - The value in the bottom-right corner of the table `dp[m][n]` will contain the final minimum edit distance.

5. **Final Result:**
   The result is the minimum number of operations required to convert `str1` into `str2`, which is stored in `dp[m][n]` after completing the dynamic programming table.

---

This approach efficiently computes the minimum edit distance using dynamic programming, avoiding the exponential time complexity of a purely recursive solution by storing intermediate results in a table.
