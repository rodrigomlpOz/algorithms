def canConstruct(ransomNote, magazine):
    # Create a hash map to count the frequency of each character in the magazine
    char_count = {}
    
    # Count characters in the magazine
    for char in magazine:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Check if we can use characters in magazine to form ransomNote
    for char in ransomNote:
        # If char is not in char_count or count is 0, we can't construct the ransom note
        if char not in char_count or char_count[char] == 0:
            return False
        # Use one instance of the character
        char_count[char] -= 1
    
    # All characters in ransomNote were successfully matched
    return True
