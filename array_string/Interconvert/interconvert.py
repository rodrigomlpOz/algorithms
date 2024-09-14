'''
EPI 6.1
'''
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

num = '-365'
ans = string_to_int(num)
print(ans)
