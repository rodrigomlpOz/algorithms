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

