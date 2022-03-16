'''
https://leetcode.com/problems/decode-ways/
'''

def numDecodings(s):
        def isPossibleDouble(num):
            return len(num) == 2 and (num[0] == '1' or (num[0] == '2' and num[1] <= '6'))
    
        if s == '':
            return 1

        if s[0] == '0':
            return 0

        possibleDouble = True if isPossibleDouble(s[:2]) else False

        if possibleDouble:
            return numDecodings(s[1:]) + numDecodings(s[2:])
        else:
            return numDecodings(s[1:])
