def base_conversion(num: str, b1: int, b2: int) -> str:
    # Helper function to convert from base `b1` to decimal (base 10)
    def convert_to_decimal(num, b1):
        is_negative = num[0] == "-"
        if is_negative:
            num = num[1:]  # Remove the negative sign for now

        total = 0
        power = 1  # To track the power of the base (b1)

        # Iterate over the number from right to left (least significant to most)
        for digit in reversed(num):
            if '0' <= digit <= '9':
                value = int(digit)
            else:  # For bases greater than 10, where digits are 'A', 'B', etc.
                value = ord(digit) - ord('A') + 10
            
            total += value * power
            power *= b1
        
        return -total if is_negative else total

    # Helper function to convert from decimal (base 10) to base `b2`
    def convert_from_decimal(num, b2):
        if num == 0:
            return "0"
        
        is_negative = num < 0
        num = abs(num)
        result = []

        while num > 0:
            remainder = num % b2
            if remainder >= 10:
                result.append(chr(ord('A') + remainder - 10))  # For digits like 'A', 'B', etc.
            else:
                result.append(str(remainder))
            num //= b2

        if is_negative:
            result.append("-")

        return ''.join(reversed(result))

    # Convert the number from base `b1` to decimal
    decimal_value = convert_to_decimal(num, b1)

    # Convert the decimal value to the desired base `b2`
    return convert_from_decimal(decimal_value, b2)
