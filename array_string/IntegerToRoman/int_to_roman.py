def int_to_roman(num):
    val = [
        1000, 900, 500, 400, 
        100, 90, 50, 40, 
        10, 9, 5, 4, 
        1
        ]
    syb = [
        "M", "CM", "D", "CD", 
        "C", "XC", "L", "XL", 
        "X", "IX", "V", "IV", 
        "I"
        ]
    roman_num = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman_num += syb[i]
            num -= val[i]
    return roman_num

# Example usage:
print(int_to_roman(3))  # Output: MCMXCIV