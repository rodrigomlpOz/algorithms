def numDecodings(s: str) -> int:
    def helper(index: int) -> int:
        # Base cases:
        if index == len(s):
            return 1  # Successfully decoded entire string
        if s[index] == '0':
            return 0  # A segment starting with '0' can't be decoded
        
        # Decode one character
        result = helper(index + 1)
        
        # Decode two characters if valid
        if index + 1 < len(s) and (s[index] == '1' or (s[index] == '2' and s[index + 1] in '0123456')):
            result += helper(index + 2)
        
        return result
    
    return helper(0)
