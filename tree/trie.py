class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            # Explicitly create a new TrieNode if it doesn't exist
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            # Explicitly check and move to the next TrieNode
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            # Explicitly check and move to the next TrieNode
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True
