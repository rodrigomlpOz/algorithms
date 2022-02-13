'''
iven n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''

def generate_paren(n):
    open = 0
    close = 0

    ans = []
    temp = []

    def recurse(open, close, n, temp, ans):
        if len(temp) == 2*n:
            ans.append(''.join(temp[:]))
        
        if open < n:
            temp.append("(")

            recurse(open+1, close, n, temp, ans)

            temp.pop()
        if close < open:
            temp.append(")")

            recurse(open, close+1, n, temp, ans)

            temp.pop()
    recurse(open, close, n, temp, ans)
    return ans
        

n = 3
a = generate_paren(n)
print(a)
