from collections import defaultdict

def findSubstring(s: str, words: list) -> list:
    if not s or not words:
        return []
    
    word_len = len(words[0])
    total_len = word_len * len(words)
    word_count = defaultdict(int)
    
    # Count the frequency of each word in the words list
    for word in words:
        word_count[word] += 1
    
    result = []
    
    # Iterate through the string and check every substring of length `total_len`
    for i in range(len(s) - total_len + 1):
        seen_words = defaultdict(int)
        j = 0
        
        # Check each word in the current window
        while j < len(words):
            word_start = i + j * word_len
            word = s[word_start:word_start + word_len]
            
            if word in word_count:
                seen_words[word] += 1
                # If the word is seen more times than it exists in the words list, break
                if seen_words[word] > word_count[word]:
                    break
            else:
                break
            j += 1
        
        # If all words match, add the starting index to the result
        if j == len(words):
            result.append(i)
    
    return result

# Example 1
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(findSubstring(s1, words1))  # Output: [0, 9]

# Example 2
s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(findSubstring(s2, words2))  # Output: []

# Example 3
s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(findSubstring(s3, words3))  # Output: [6, 9, 12]
