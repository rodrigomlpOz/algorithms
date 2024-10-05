# Step 2: Convert from decimal (base 10) to base b2
def convert_from_decimal(num: int, b2: int) -> str:
    # If the number is 0, return "0" (since any base conversion of 0 is 0)
    if num == 0:
        return "0"
    
    # Check if the number is negative
    is_negative = num < 0
    # Work with the absolute value of the number for conversion
    num = abs(num)
    
    # This list will store the digits (or characters) of the result in reverse order
    result = []

    # Perform the conversion by repeatedly dividing by the base b2
    while num > 0:
        # Get the remainder when dividing by the base (this gives the next least significant digit)
        remainder = num % b2
        
        # If the remainder is 10 or greater, it represents a letter (A = 10, B = 11, etc.)
        if remainder >= 10:
            # Convert the remainder to the corresponding letter and append it to the result
            result.append(chr(ord('A') + remainder - 10))  # 'A' represents 10, 'B' represents 11, etc.
        else:
            # If the remainder is less than 10, just append the number as a string
            result.append(str(remainder))
        
        # Update num by dividing it by the base b2 to move to the next digit
        num //= b2

    # If the original number was negative, add the negative sign
    if is_negative:
        result.append('-')

    # Since the digits were generated in reverse order (from least to most significant),
    # reverse the result list and join it into a string
    return ''.join(reversed(result))
