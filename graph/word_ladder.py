import collections
import string
def word_ladder(beginWord, endWord, wordList):
    q = collections.deque([])
    q.append([beginWord, 1])
    wordList = set(wordList)
    while q:
        word, word_count = q.popleft()
        if word == endWord:
            return word_count
        for i in range(len(word)):
            for letter in string.ascii_lowercase:
                curr_word = word[:i] + letter + word[i+1:]
                if curr_word in wordList:
                    wordList.remove(curr_word)
                    q.append([curr_word, word_count+1])
    return 0 


        

beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
i = word_ladder(beginWord, endWord, wordList)
print(i)