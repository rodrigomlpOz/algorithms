def word_break(s, wordDict):
    def recurse(s, wordDict):
        if not s:
            return True
        else:
            for i in range(1, len(s)+1):
                if s[:i] in wordDict and recurse(s[i:], wordDict):
                    return True
            return False
    return recurse(s, wordDict)

def word_break_dp(s, wordDict):
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(len(s)):
        if dp[i]:
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    dp[j] = True
        
    return dp[-1]

s = "applepenapple"
wordDict = ["apple", "pen"]
word_break_dp(s, wordDict)
