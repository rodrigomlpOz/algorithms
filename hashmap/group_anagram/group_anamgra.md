
# Group Anagrams

## Problem Description

Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.

## Function Definition

```python
def groupAnagrams(strs):
    # Implementation goes here
    pass
```

## Example Calls

```python
# Example 1
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Example 2
print(groupAnagrams([""]))
# Output: [[""]]

# Example 3
print(groupAnagrams(["a"]))
# Output: [["a"]]
```

## High-Level Solution Approach

1. **Sorting or Character Count**: 
   - For each word, create a signature that identifies its anagram group. A common approach is to sort the characters of the word or create a frequency count of its characters.
   
2. **Mapping to Groups**:
   - Use a dictionary to map each signature (sorted word or character count) to a list of words that belong to the same anagram group.
   
3. **Collect Results**:
   - Finally, extract the lists of grouped anagrams from the dictionary and return them as the result.

---

