'''
EPI 6.2
'''

import string
def base_conversion(num, b1, b2):
    def convert_to_decimal(num, b1):
        ans = 0
        is_negative = False
        if num[0] == "-":
            num, is_negative = num[1:], True
        for i in range(len(num)):
            ans = (ans*b1) + string.hexdigits.index(num[i].lower())
        return -ans if is_negative else ans
    def convert_to_base(num, b2):
        is_negative = False
        if num < 0:
            is_negative, num = True, abs(num)
        ans = ''
        while num > 0:
            ans += string.hexdigits[(num % b2)].upper()
            num //= b2
        return ('-' if is_negative else '') + ''.join(reversed(ans))
            
    ans = convert_to_decimal(num, b1)
    return convert_to_base(ans, b2)



n = "-8"
b1 = 10
b2 = 2
ans = base_conversion(n, b1, b2)
print(ans)
