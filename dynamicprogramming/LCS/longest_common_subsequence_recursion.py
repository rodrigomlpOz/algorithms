def LCS(text1, text2):
    def recurse(text1, text2):
        if not text1 or not text2:
            return 0
        elif text1[0] == text2[0]:
            return 1 + recurse(text1[1:], text2[1:])
        else:
            return max(recurse(text1[1:],text2), recurse(text1, text2[1:]))
    return recurse(text1, text2)

    
'''
Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''
text1 = "abcde"
text2 = "ace" 
ans = LCS(text1, text2)
print(ans)
