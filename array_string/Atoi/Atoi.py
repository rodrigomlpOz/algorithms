def myAtoi(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    i = 0
    n = len(s)
    
    # Step 1: Discard leading whitespaces
    while i < n and s[i].isspace():
        i += 1
    
    if i == n:
        return 0
    
    # Step 2: Check for optional sign
    sign = 1
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
    
    # Step 3: Convert numerical characters
    num = 0
    while i < n and '0' <= s[i] <= '9':
        digit = ord(s[i]) - ord('0')
        # Check for overflow and underflow
        num = num * 10 + digit

        # Overflow check after adding the new digit
        if sign * num > INT_MAX:
            return INT_MAX
        elif sign * num < INT_MIN:
            return INT_MIN
        i += 1
    
    return max(INT_MIN, min(sign * num, INT_MAX))

# Example usage
print(myAtoi("42"))            # Output: 42
print(myAtoi("   -42"))        # Output: -42
print(myAtoi("4193 with words"))  # Output: 4193
print(myAtoi("words and 987")) # Output: 0
print(myAtoi("-91283472332"))  # Output: -2147483648 (INT_MIN)
