def bracketMatch(text):
    open_brackets = 0  # Tracks unbalanced opening brackets
    unmatched_closing = 0  # Tracks unmatched closing brackets
    
    for char in text:
        if char == '(':
            open_brackets += 1
        elif char == ')':
            if open_brackets > 0:
                open_brackets -= 1
            else:
                unmatched_closing += 1
                
    # The total number of insertions needed is the sum of unmatched closing and unbalanced opening brackets
    return open_brackets + unmatched_closing


# Test cases
print(bracketMatch("(((")) # Expected output: 3
print(bracketMatch("(()"))  # Expected output: 1
print(bracketMatch(")("))   # Expected output: 2
print(bracketMatch("()"))   # Expected output: 0
print(bracketMatch("(())()")) # Expected output: 0
print(bracketMatch("())(()")) # Expected output: 2
