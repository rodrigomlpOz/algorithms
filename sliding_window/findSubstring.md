### Problem Statement:
You are given a string `s` and a list of words `words`, where each word in `words` is of the same length. Your task is to find all starting indices of substring(s) in `s` that are a concatenation of each word in `words` exactly once, in any order, without any intervening characters.

Return the starting indices in any order.

### Function Signature:
```python
def findSubstring(s: str, words: list) -> list:
```

### Function Calls:
```python
# Example 1
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))  # Output: [0, 9]

# Example 2
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words))  # Output: []

# Example 3
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words))  # Output: [6, 9, 12]
```

### High-Level Solution:

1. **Understand the Input**:
   - We are given a string `s` and a list of words `words` where each word has the same length.
   - We need to find the starting indices of substrings in `s` that consist of a concatenation of all the words in `words`, in any order.

2. **Calculate Window Size**:
   - The total window size to check in `s` is the sum of the lengths of all the words in `words`. This is `total_len = num_words * word_len`, where `num_words` is the number of words, and `word_len` is the length of each word.

3. **Sliding Window with Word Counting**:
   - For each starting index `i` in `s`, extract a window of size `total_len` and split it into chunks of length `word_len`.
   - Use a dictionary `seen_words` to count how many times each word appears in this window and compare it to the expected word counts in `words` (stored in a dictionary `word_count`).
   - If all the words in the window match the counts in `words`, record the starting index `i` as valid.

4. **Return the Result**:
   - Return the list of all valid starting indices where the substrings match the criteria.

### Final Function:
```python
from collections import defaultdict

def findSubstring(s: str, words: list) -> list:
    pass
```
