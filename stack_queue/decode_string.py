import string
def decodeString(s: str) -> str:
    stack = []
    
    alphas, digits = '', ''

    for c in s:
        if c.isdigit():
            digits += c
        elif c == '[':
            stack.append((alphas, int(digits)))
            alphas, digits = '', ''
        elif c == ']':
            prev, n = stack.pop()
            alphas = prev + alphas * n
        elif c.isalpha():
            alphas += c

    return alphas
