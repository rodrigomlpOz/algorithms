import string
def int_to_string(num):
    is_negative = False
    if num < 0:
        num , is_negative = -num,  True
    ans = []

    while num > 0:
        ans += chr(ord("0") + (num % 10))
        num //= 10
    return ('-' if is_negative else '') +  (''.join(reversed(ans)))

ans = int_to_string(-345)
print(ans)

def string_to_int(num):
    is_negative = 0
    ans = 0
    if num[0] == "-":
        is_negative = 1
    num = num[is_negative:]
    for digit in num:
        ans = (ans*10) + string.digits.index(digit)
    return -ans if is_negative else ans

num = '-365'
ans = string_to_int(num)
print(ans)