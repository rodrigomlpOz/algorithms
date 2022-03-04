'''
Diif between two strings

'''

def lcs(m, n):
    dp = [[0]*(len(m)+1) for _ in range(len(n)+1)]
    for i in range(len(n)+1):
            dp[i][0] = 0
    for j in range(len(m)+1):
            dp[0][j] = j
    for i in range(1, len(n)+1):
        for j in range(1, len(m)+1):
            if n[i-1] == m[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp

def diffBetweenTwoStrings(source, target):
    dp = lcs(source, target)
    ans = []
    i = 1
    j = 1
    # We are always considering strings source[i:] and target[j:]
    while i < (len(source)+1) and j < (len(target)+1):
        if source[i-1] == target[j-1]:
            # Write the string with no edits
            ans.append(source[i-1])
            i += 1
            j += 1
        else:
            # We have to decide whether to subtract source[i],
            # or add target[j].
            if dp[i-1][j] <= dp[i][j-1]:
                ans.append('-' + source[i-1])
                i += 1
            else:
                ans.append('+' + target[j-1])
                j += 1

    while j < (len(target)+1):
        ans.append('+' + target[j-1])
        j += 1

    return " ".join(ans)

print(diffBetweenTwoStrings("AB", "ABDFFGH"))
