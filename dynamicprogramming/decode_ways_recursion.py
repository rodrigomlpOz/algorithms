'''
https://leetcode.com/problems/decode-ways/
'''

def decode_ways(word):
    def recurse(word):
        if not word:
            return 1
        if len(word) <= 1:
            return 1 if word[0] != '0' else 0
        else:
            for _ in range(len(word)-1):
                one_digit = recurse(word[1:]) if word[0] != '0' else 0
                two_digit = recurse(word[2:]) if 10 <= int(word[:2]) <= 26 else 0
                return one_digit + two_digit
    return recurse(word)

'''
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12)
.
'''
ans = decode_ways("01")
print(ans)
