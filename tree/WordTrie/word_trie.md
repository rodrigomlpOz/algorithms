Here's the skeleton for the `WordDictionary` class that supports adding new words and searching for existing words. The `search` function will need to handle the case where a word may contain the wildcard character `.` which can be matched with any letter.

### Skeleton for `WordDictionary` Class:

```python
from collections import defaultdict

class WordDictionaryNode:
    def __init__(self):
        # Initialize children and is_word flag
        pass

class WordDictionary:
    def __init__(self):
        # Initialize the root node
        pass

    def addWord(self, word: str):
        # Adds a word into the WordDictionary
        pass

    def search(self, word: str) -> bool:
        # Search for a word in the WordDictionary, where '.' can be any letter
        pass
```

### Example Function Calls:

```python
word_dict = WordDictionary()

# Add words
word_dict.addWord("bad")
word_dict.addWord("dad")
word_dict.addWord("mad")

# Search for exact words
print(word_dict.search("pad"))  # Should return False
print(word_dict.search("bad"))  # Should return True

# Search with wildcards
print(word_dict.search(".ad"))  # Should return True (matches "bad", "dad", or "mad")
print(word_dict.search("b.."))  # Should return True (matches "bad")
```

### High-Level Plan:

1. **Word Insertion (`addWord`)**:
   - For each character in the word, move through the Trie. If the character does not exist in the current node’s children, create a new node.
   - At the end of the word, mark the node as a word (i.e., set `is_word = True`).

2. **Word Search (`search`)**:
   - If the word contains only regular characters, simply traverse the Trie and check if the word exists.
   - If the word contains `.` characters, treat `.` as a wildcard that can match any character. For each `.`, recursively check all possible paths in the Trie.

You can implement the detailed logic inside the functions now based on this skeleton.
