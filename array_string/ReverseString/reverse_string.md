**Problem Statement**

Given an input string `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space. Return a string of the words in reverse order concatenated by a single space.

**Example 1:**

Input: 
```
s = "the sky is blue"
```
Output: 
```
"blue is sky the"
```

**Example 2:**

Input: 
```
s = "  hello world  "
```
Output: 
```
"world hello"
```
Explanation: Your reversed string should not contain leading or trailing spaces.

**Example 3:**

Input: 
```
s = "a good   example"
```
Output: 
```
"example good a"
```
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

**Example 4:**

Input:
```
s = "  Bob    Loves  Alice   "
```
Output:
```
"Alice Loves Bob"
```

**Example 5:**

Input:
```
s = "Alice does not even like bob"
```
Output:
```
"bob like even not does Alice"
```

### Solution

The provided solution follows these steps:
1. **Trim Spaces**: It removes leading and trailing spaces and reduces multiple spaces between words to a single space.
2. **Reverse Entire String**: It reverses the entire string.
3. **Reverse Each Word**: It reverses each word in the reversed string to restore the correct word order but in reversed positions.

