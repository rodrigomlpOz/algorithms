from collections import defaultdict, Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    # Frequency map of characters in t
    t_count = Counter(t)
    required = len(t_count)
    
    # Left and right pointers for the sliding window
    left, right = 0, 0
    # Keep track of how many characters in the current window have the desired frequency
    formed = 0
    window_counts = defaultdict(int)
    
    # (window_length, left, right) for the smallest valid window
    ans = float("inf"), None, None
    
    while right < len(s):
        # Add the current character from s to the window
        character = s[right]
        window_counts[character] += 1
        
        # If the frequency of the current character in the window matches the frequency in t
        if character in t_count and window_counts[character] == t_count[character]:
            formed += 1
        
        # Try to contract the window until it ceases to be 'desirable'
        while left <= right and formed == required:
            character = s[left]
            
            # Update the result if this window is smaller than previously found ones
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # Remove the character from the window and move left pointer
            window_counts[character] -= 1
            if character in t_count and window_counts[character] < t_count[character]:
                formed -= 1
            
            left += 1
        
        # Move right pointer forward
        right += 1
    
    # If no valid window is found, ans[0] will still be infinity (set at the beginning).
    # In that case, we return an empty string as no window contains all characters.
    if ans[0] == float("inf"):
        return ""

    # If a valid window was found, ans contains the smallest window length
    # and the indices of the start and end of that window.
    # We return the substring from the start (ans[1]) to the end (ans[2]).
    else:
        return s[ans[1]: ans[2] + 1]

