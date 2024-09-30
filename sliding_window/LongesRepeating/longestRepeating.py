from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_count = 0  # To track the max frequency of any single character in the window
    char_count = defaultdict(int)  # To count the frequency of characters in the current window
    max_length = 0  # To store the length of the longest valid substring
    
    for right in range(len(s)):
        # Increment the count of the current character
        char_count[s[right]] += 1
        # Update the max_count of the most frequent character in the current window
        max_count = max(max_count, char_count[s[right]])
        
        # If the number of replacements needed exceeds k, shrink the window
        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1  # Reduce the count of the left character
            left += 1  # Shrink the window from the left
        
        # Update the max_length to be the size of the current valid window
        max_length = max(max_length, right - left + 1)
    
    return max_length
