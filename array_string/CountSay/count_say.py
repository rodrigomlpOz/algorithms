'''
EPI 6.8
'''

def count_say(n):
    def next_say(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)



    ans = "1"
    for _ in range(1, n):
        ans = next_say(ans)
    return ans

count_say(4)
