def calculate(s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":

                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)

print(calculate("3+2*2"))        # Output: 7
print(calculate(" 3/2 "))        # Output: 1
print(calculate(" 3+5 / 2 "))    # Output: 5
print(calculate("10+2*6"))       # Output: 22
print(calculate("100*2+12"))     # Output: 212
print(calculate("100*(2+12)/14"))# Output: 200
print(calculate("1+1+1"))        # Output: 3
print(calculate("1-1+1"))        # Output: 1
print(calculate("14-3/2"))       # Output: 13
print(calculate("3+2*2-4/2"))    # Output: 5
