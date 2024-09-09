def isMatch(s: str, p: str) -> bool:
    # Base Case: if pattern is empty, check if the string is also empty
    if not p:
        return not s
    
    # Check if the first characters match (including '.')
    first_match = bool(s) and (p[0] == s[0] or p[0] == '.')
    
    # If the second character of pattern is '*', we have two options
    if len(p) >= 2 and p[1] == '*':
        # Option 1: Skip the '*' and preceding character in the pattern (match 0 of the preceding character)
        # Option 2: Use '*' to match 1 or more of the preceding character
        return (isMatch(s, p[2:]) or  # Skip '*' and its preceding element
                (first_match and isMatch(s[1:], p)))  # Use '*' and consume one character of the string
    
    # If no '*', we just move to the next character in both string and pattern
    else:
        return first_match and isMatch(s[1:], p[1:])

# Example calls:
print(isMatch("aa", "a*"))  # Output: True
print(isMatch("ab", ".*"))  # Output: True
print(isMatch("aab", "c*a*b"))  # Output: True
