class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.isEndOfWord
            
            char = word[i]
            if char == '.':
                # If we encounter a dot, check all possible nodes at this level
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # If it's a regular character, just proceed to the next node
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
        
        return dfs(self.root, 0)
