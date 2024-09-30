from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_count = 0
    char_count = defaultdict(int)  # Using defaultdict to simplify the code
    
    for right in range(len(s)):
        # Increment the count of the current character
        char_count[s[right]] += 1
        # Track the max frequency of any character in the current window
        max_count = max(max_count, char_count[s[right]])
        
        # If the number of characters to replace exceeds k, shrink the window
        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1
    
    return len(s) - left  # The largest valid window
