def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove leading zeros
    start = 0
    while start < len(result) - 1 and result[start] == 0:
        start += 1

    result = result[start:]
    return [sign * result[0]] + result[1:] if result else [0]

# Example usage
num1 = [1, 2, 3]
num2 = [4, 5, 6]
print(multiply(num1, num2))  # Output: [5, 6, 0, 8, 8]
