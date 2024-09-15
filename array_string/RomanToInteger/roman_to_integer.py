def romanToInt(self, s: str) -> int:
    # Dictionary to map Roman numerals to their respective integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize total to 0
    total = 0
    
    # Traverse the Roman numeral string
    for i in range(len(s)):
        # If the current numeral is smaller than the next one, subtract it
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            # Otherwise, add the current numeral's value
            total += roman_map[s[i]]
    
    return total