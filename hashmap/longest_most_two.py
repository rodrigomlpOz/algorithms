import collections
def longest_at_most_two(s):
    if len(s) < 3:
        return len(s)

    left = 0
    right = 0
    dict = collections.defaultdict(int)
    longest_size = 2
    while right < len(s):
        dict[s[right]] = right 
        right += 1
        if len(dict) > 2:
            idx = min(dict.values())
            del dict[s[idx]]
            left = idx + 1
        longest_size = max(longest_size, right - left)
    return longest_size

        
s = "ccaabbb"
ans = longest_at_most_two(s)
print(ans)

'''
Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
'''