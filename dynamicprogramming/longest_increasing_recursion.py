def longest_palindrome_subseque(s):
    def recurse(l, r, s):
        if l == r:
            return 1
        if l > r:
            return 0
        return (2 + recurse(l+1, r-1, s)) if s[l] == s[r] else max(recurse(l+1, r, s), recurse(l, r-1, s))
    return recurse(0, len(s)-1, s)
s = "cbbd"
ans = longest_palindrome_subseque(s)
print(ans)