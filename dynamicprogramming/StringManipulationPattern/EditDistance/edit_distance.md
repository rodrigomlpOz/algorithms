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

### Explanation of the Recursive Formula for **Edit Distance**:

The recursive formula for the **edit distance** problem expresses how we can transform one string into another by performing a series of operations: **insertion**, **deletion**, and **substitution**. The formula computes the minimum number of operations needed by considering these three possibilities at every step.

### Recursive Formula:

For two strings `str1` of length `m` and `str2` of length `n`, the recursive relation is:

\[
\text{editDistance}(str1, str2, m, n) = \min \left\{
       \begin{array}{c}
       \text{editDistance}(str1, str2, m, n-1) + 1 \quad \text{(Insertion)} \\
       \text{editDistance}(str1, str2, m-1, n) + 1 \quad \text{(Deletion)} \\
       \text{editDistance}(str1, str2, m-1, n-1) + \text{cost} \quad \text{(Substitution)}
       \end{array}
   \right.
\]
Where:
- `cost` is `0` if the characters `str1[m-1]` and `str2[n-1]` are the same, and `1` if they are different.

### Explanation of Each Operation:

1. **Insertion:**
   - We can insert a character from `str2` into `str1` to match the character at the current position `n` of `str2`.
   - If we insert the character `str2[n-1]`, the remaining problem becomes transforming `str1[0..m]` into `str2[0..n-1]`, which has one fewer character in `str2`.
   - The cost of insertion is `1` because we are adding one new character to `str1`.

   \[
   \text{editDistance}(str1, str2, m, n-1) + 1
   \]

2. **Deletion:**
   - We can delete a character from `str1` to match the character at the current position `n` of `str2`.
   - If we delete the character `str1[m-1]`, the remaining problem becomes transforming `str1[0..m-1]` into `str2[0..n]`, which has one fewer character in `str1`.
   - The cost of deletion is `1` because we are removing one character from `str1`.

   \[
   \text{editDistance}(str1, str2, m-1, n) + 1
   \]

3. **Substitution:**
   - We can replace the current character in `str1` with the character from `str2`. This is called substitution.
   - If the characters at `str1[m-1]` and `str2[n-1]` are the same, no substitution is needed, and the cost is `0`.
   - If the characters differ, we substitute `str1[m-1]` with `str2[n-1]`, and the cost is `1`.
   - After the substitution, the remaining problem becomes transforming `str1[0..m-1]` into `str2[0..n-1]`.

   \[
   \text{editDistance}(str1, str2, m-1, n-1) + \text{cost}
   \]

   Where `cost = 0` if `str1[m-1] == str2[n-1]`, and `cost = 1` otherwise.

---

### Base Case:

The base cases arise when one of the strings is empty:
1. **If `m == 0` (i.e., `str1` is empty):**
   - We must insert all characters of `str2` into `str1`, so the cost is `n` (the length of `str2`).
   \[
   \text{editDistance}("", str2, 0, n) = n
   \]
   
2. **If `n == 0` (i.e., `str2` is empty):**
   - We must delete all characters of `str1`, so the cost is `m` (the length of `str1`).
   \[
   \text{editDistance}(str1, "", m, 0) = m
   \]

### Example Walkthrough:

Let’s compute the edit distance between `str1 = "kitten"` and `str2 = "sitting"` using this recursive formula:

#### Step 1:
- Compare `str1[5] = "n"` and `str2[6] = "g"`.
- They are different, so we have three options:
  1. Insert `g` into `str1`: Solve `editDistance("kitten", "sittin")`.
  2. Delete `n` from `str1`: Solve `editDistance("kitte", "sitting")`.
  3. Substitute `n` with `g`: Solve `editDistance("kitte", "sittin")`.

- Pick the option with the minimum cost, add 1 for the operation performed.

#### Step 2:
Continue comparing characters and apply the same logic recursively until the base cases are reached.

### Conclusion:
This recursive formula systematically explores all possible ways to convert one string into another by either inserting, deleting, or substituting characters. The result is the minimum number of operations required, which is known as the **edit distance**.
