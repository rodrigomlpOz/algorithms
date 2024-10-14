from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # When a word ends at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Mark the end of a word

def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    # Build the Trie
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    result = []
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    
    def backtrack(row: int, col: int, parent: TrieNode):
        letter = board[row][col]
        curr_node = parent.children[letter]
        
        # Check if we found a word
        if curr_node.word:
            result.append(curr_node.word)
            curr_node.word = None  # Avoid duplicate entries
        
        # Mark the current cell as visited
        board[row][col] = '#'  # Temporary marker
        
        # Explore neighbors: up, down, left, right
        for (row_offset, col_offset) in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_row, new_col = row + row_offset, col + col_offset
            if (0 <= new_row < rows and
                0 <= new_col < cols and
                board[new_row][new_col] in curr_node.children):
                backtrack(new_row, new_col, curr_node)
        
        # Restore the original letter after backtracking
        board[row][col] = letter
        
        # ### Optimization: remove the leaf node
        # If the current Trie node has no children after backtracking,
        # it means no further words can be formed from this path.
        # Therefore, we remove this node from its parent to prune the Trie,
        # which reduces the search space and improves efficiency.
        # if not curr_node.children:
        #     del parent.children[letter]
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] in trie.root.children:
                backtrack(row, col, trie.root)
    return result

# Example Usage
if __name__ == "__main__":
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
words = ["oath","pea","eat","rain"]
found_words = find_words(board, words)
print(found_words)  # Output: ["eat","oath"]
