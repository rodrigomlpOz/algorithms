from collections import defaultdict

def groupAnagrams(strs):
    # Dictionary to store the grouped anagrams
    anagram_groups = defaultdict(list)
    
    for word in strs:
        # Sort the word and use it as the key
        sorted_word = ''.join(sorted(word))
        # Append the original word to the list corresponding to the sorted key
        anagram_groups[sorted_word].append(word)
    
    # Return the grouped anagrams as a list of lists
    return list(anagram_groups.values())
