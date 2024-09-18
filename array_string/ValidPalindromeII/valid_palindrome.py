def validPalindrome(s: str) -> bool:
    def is_palindrome_range(s, i, j):
        """Check if the substring s[i:j+1] is a palindrome."""
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    # Two pointer approach
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Try skipping either the left or right character
            return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
        left += 1
        right -= 1
    
    return True