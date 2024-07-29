## Problem Statement

Given a string `word`, partition the string such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `word`.

## Function Signature

```python
def palindrome_partitioning(word):
    pass
```

### Input Parameters

- `word`: A string containing the input word to be partitioned.

### Output

- A list of lists, where each inner list represents a unique palindrome partitioning of the input word.

### Example Inputs and Outputs

**Example 1:**

- **Input:** `word = "aab"`
- **Output:** `[["aa", "b"], ["a", "a", "b"]]`

## High-Level Approach

1. **Palindrome Check**: Define a helper function `is_palindrome` to check if a given substring is a palindrome. This function can check if a string is equal to its reverse.

2. **Backtracking**: Use backtracking to explore all possible partitions of the word. For each possible partition, check if the substring is a palindrome. If it is, add it to the current partition (`temp`) and recursively process the remaining substring.

3. **Recursive Function `recurse`**:
    - **Parameters**:
      - `word`: The remaining part of the string to be partitioned.
      - `temp`: A list representing the current partitioning of palindromic substrings.
      - `ans`: The list to store all valid palindrome partitions.
    - **Process**:
      - If the remaining string (`word`) is empty, it means a valid partition has been found, and `temp` should be added to `ans`.
      - Iterate over the string, generating substrings and checking each substring to see if it is a palindrome. If it is, add the substring to `temp`, recursively partition the remaining string, and then backtrack by removing the last added substring from `temp`.

### Function Implementation (without the actual code)

The `palindrome_partitioning` function initializes the list `ans` to store the results and calls the recursive function `recurse` to explore all possible partitions of the string. The backtracking approach ensures that all potential partitions are considered, and palindromic partitions are collected without duplicates. The `is_palindrome` helper function is used to check whether a substring is palindromic before proceeding with the partitioning.
