def isPalindrome(s: str) -> bool:
    # Step 1: Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Use two pointers to check if the cleaned string is a palindrome
    left, right = 0, len(cleaned_s) - 1
    
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
    
    return True