def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    
    previous = "1"
    for _ in range(n - 1):
        current = ""
        count = 1
        for j in range(1, len(previous)):
            if previous[j] == previous[j - 1]:
                count += 1
            else:
                current += str(count) + previous[j - 1]
                count = 1
        current += str(count) + previous[-1]
        previous = current
    
    return previous

print(countAndSay(1))  # Output: "1"
print(countAndSay(2))  # Output: "11"
print(countAndSay(3))  # Output: "21"
print(countAndSay(4))  # Output: "1211"
print(countAndSay(5))  # Output: "111221"
print(countAndSay(6))  # Output: "312211"
print(countAndSay(7))  # Output: "13112221"
print(countAndSay(8))  # Output: "1113213211"
print(countAndSay(9))  # Output: "31131211131221"
print(countAndSay(10)) # Output: "13211311123113112211"
