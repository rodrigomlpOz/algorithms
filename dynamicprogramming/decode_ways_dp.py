'''
A -> 1 .... Z -> 26

1261 can be

"AZB"
"ABFB"
"LFB"

'''

def decode_ways(S):
    if not S:
        return 0
    dp = [0 for _ in range(len(S)+1)]
    dp[0] = 1
    dp[1] = 0 if S[0] == "0" else 1
    for i in range(2, len(S)+1):
        dp[i] = dp[i-1]
        if 10 <= int(S[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    return dp[len(S)]
        

S = "1261"

r = decode_ways(S)
print(r)