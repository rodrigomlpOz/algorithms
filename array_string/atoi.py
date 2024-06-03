'''
Problem:
https://www.geeksforgeeks.org/write-your-own-atoi/
'''

def myAtoi(str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        sign = 1 
        if not str or str[0].isalpha():
            return 0
        else:
            if str[0] == "+":
                str = str[1:]
            elif str[0] == "-":
                str = str[1:]
                sign = -1
            num = 0 
            i = 0
            while i < len(str) and str[i].isdigit():
                    num = num * 10 + (ord(str[i])-ord('0'))
                    i += 1
            return max(-2**31, min(sign * num,2**31-1))



# Example usage
print(myAtoi("12345"))      # Output: 12345
print(myAtoi("-6789"))      # Output: -6789
print(myAtoi("123abc"))     # Output: 123
print(myAtoi("abc123"))     # Output: 0
print(myAtoi(""))           # Output: 0
print(myAtoi("   -42"))     # Output: -42
print(myAtoi("4193 with words"))  # Output: 4193
print(myAtoi("words and 987"))    # Output: 0
print(myAtoi("-91283472332"))     # Output: -2147483648 (clamped to 32-bit int)
