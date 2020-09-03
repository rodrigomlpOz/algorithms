def word_break_dp(s, wordDict):
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j]:
                if s[j:i] in wordDict:
                    dp[i] = True
    return dp[-1]

s = "leetcode"
wordDict = ["leet", "code"]
ans = word_break_dp(s, wordDict)
print(ans)
'''
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
'''