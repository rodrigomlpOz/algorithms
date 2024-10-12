def base_conversion(num: str, b1: int, b2: int) -> str:
    # Convert from base `b1` to base 10
    def convert10(num, b1):
        ans = 0
        is_negative = (num[0] == '-')
        num = num[1:] if is_negative else num

        for i in range(len(num)):
            if '0' <= num[i] <= '9':
                ans = b1 * ans + (ord(num[i]) - ord('0'))
            else:
                ans = b1 * ans + (ord(num[i].lower()) - ord('a') + 10)
        
        return -ans if is_negative else ans

    # Convert from base 10 to base `b2`
    def convertBase(num, base):
        if num == 0:
            return "0"
        
        is_negative = (num < 0)
        num = abs(num)
        ans = ""

        while num > 0:
            digit = num % base
            if digit < 10:
                ans = chr(digit + ord('0')) + ans
            else:
                ans = chr(digit - 10 + ord('A')) + ans
            num //= base
        
        return ("-" + ans) if is_negative else ans

    # Convert the number from base `b1` to base 10
    base10 = convert10(num, b1)
    # Convert from base 10 to base `b2`
    result = convertBase(base10, b2)
    
    return result

# Test examples
print(base_conversion('132', 5, 3))  # Example 5: Output should be "1102"
print(base_conversion('-11', 10, 2))  # Example 6: Output should be "-1011"
print(base_conversion('Z', 36, 10))  # Example 7: Output should be "35"
print(base_conversion('35', 10, 36))  # Example 8: Output should be "Z"
print(base_conversion('17', 8, 16))  # Example 9: Output should be "F"
print(base_conversion('123456789', 10, 2))  # Example 10: Output should be "111010110111100110100010101"
