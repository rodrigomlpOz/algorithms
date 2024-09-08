### Problem: Word Ladder (Leetcode 127)

The task is to transform a given `beginWord` into a target `endWord` by changing exactly one letter at a time. Each transformed word must exist in the provided `wordList`. The objective is to find the shortest transformation sequence from `beginWord` to `endWord`.

### Problem Definition:
- **Input**:
  - `beginWord`: Starting word.
  - `endWord`: Target word that we need to reach.
  - `wordList`: A list of valid words that can be used during the transformation.

- **Output**:
  - The length of the shortest transformation sequence from `beginWord` to `endWord`.
  - If no such transformation is possible, return `0`.

### High-Level Solution:

1. **Graph Representation**:
   - Treat each word as a node and an edge exists between two nodes if they differ by exactly one letter. 
   - The problem can be viewed as finding the shortest path in an unweighted graph where nodes are words and edges represent valid transformations.

2. **Breadth-First Search (BFS)**:
   - Use BFS since it guarantees finding the shortest path in an unweighted graph.
   - Starting from `beginWord`, explore all words that can be transformed by changing one letter. Continue until either `endWord` is found or all possibilities are exhausted.
   
3. **Word List as Set**:
   - Convert the `wordList` into a set for O(1) lookups. This allows us to efficiently check if a word is in the list and mark it as visited (by removing it from the set).

4. **Neighbor Generation**:
   - For each word, generate its neighbors by changing each letter to every possible lowercase letter (`'a'` to `'z'`) and check if the resulting word is in the `wordList`.

### Function Definition:

```python
def word_ladder(beginWord, endWord, wordList):
    """
    Finds the shortest transformation sequence from beginWord to endWord using BFS.
    
    :param beginWord: Starting word for the transformation.
    :param endWord: Target word that needs to be reached.
    :param wordList: List of valid words that can be used during the transformation.
    :return: The length of the shortest transformation sequence, or 0 if no sequence exists.
    """
    pass  # High-level logic explained above
```

### Steps in the Solution:

1. **Initialize BFS Queue**:
   - Use a queue to keep track of words and their corresponding transformation counts (i.e., depth of BFS).
   
2. **Process Words**:
   - For each word in the queue, generate all possible one-letter transformations. If the transformation matches `endWord`, return the transformation count.
   
3. **Remove Visited Words**:
   - Once a word is processed, remove it from the `wordList` to avoid revisiting.

4. **Return 0 if No Path Found**:
   - If the queue is exhausted without finding `endWord`, return `0`.

### Function Calls:

#### Example 1:
```python
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

i = word_ladder(beginWord, endWord, wordList)
print(i)  # Expected Output: 5 (hit -> hot -> dot -> dog -> cog)
```

#### Example 2:
```python
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]

i = word_ladder(beginWord, endWord, wordList)
print(i)  # Expected Output: 0 (No valid transformation path)
```

### Time Complexity:
- **Time Complexity**: O(M^2 * N), where M is the length of each word and N is the number of words in the `wordList`. For each word, we generate all possible transformations, which takes O(M) time, and for each transformation, we search through the word list, which also takes O(M) for each of N words.

### Space Complexity:
- **Space Complexity**: O(N), where N is the number of words in the `wordList`, for storing the queue and visited words.

This BFS-based solution efficiently finds the shortest path from `beginWord` to `endWord` using valid transformations from `wordList`.
