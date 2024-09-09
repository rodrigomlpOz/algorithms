def isMatch(s: str, p: str) -> bool:
    def helper(i: int, j: int) -> bool:
        # Base cases
        if j == len(p):  # If we reached the end of the pattern
            return i == len(s)  # True if we've also consumed the entire string
        
        if i == len(s):  # If we reached the end of the string
            # Pattern can match only if remaining pattern consists of '*'
            return all(x == '*' for x in p[j:])
        
        # Recursive cases
        if p[j] == '*':
            # '*' matches zero or more characters
            return helper(i + 1, j) or helper(i, j + 1)
        
        if p[j] == '?' or p[j] == s[i]:
            # '?' matches any character or exact match for current character
            return helper(i + 1, j + 1)
        
        # If no match, return False
        return False
    
    # Start recursion from the beginning of both strings
    return helper(0, 0)
