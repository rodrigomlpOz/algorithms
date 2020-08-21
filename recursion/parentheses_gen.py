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