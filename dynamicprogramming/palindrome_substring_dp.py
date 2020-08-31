def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        res = ''
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = ((s[i] == s[j]) and ((j - i <= 2) or dp[i+1][j-1]))
                if dp[i][j]:
                    if (j-i+1) > max:
                        max = j-i+1
                        res = s[i:j+1]
        return res
s = "babad"
ans = longestPalindrome(s)
print(ans)