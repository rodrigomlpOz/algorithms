from collections import defaultdict

def findSubstring(s: str, words: list) -> list:
    if not s or not words:
        return []
    
    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_count = defaultdict(int)
    
    # Create the word frequency map
    for word in words:
        word_count[word] += 1
    
    result = []
    
    # Iterate over each possible starting point
    for i in range(len(s) - total_len + 1):
        seen_words = defaultdict(int)
        j = 0
        
        # Check if the substring from i to i + total_len is valid
        while j < num_words:
            word_start = i + j * word_len
            word = s[word_start:word_start + word_len]
            
            if word in word_count:
                seen_words[word] += 1
                
                # If the count exceeds the expected count, break
                if seen_words[word] > word_count[word]:
                    break
            else:
                break
            
            j += 1
        
        # If all words matched exactly, store the starting index
        if j == num_words:
            result.append(i)
    
    return result
