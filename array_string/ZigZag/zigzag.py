def convert(s: str, numRows: int) -> str:
    # Edge case: If numRows is 1 or greater than the length of s
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize a list to hold each row's characters
    rows = [''] * numRows
    current_row = 0
    going_down = False

    # Iterate through each character in the string
    for char in s:
        rows[current_row] += char
        # Change direction if we are at the first or last row
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        # Move up or down
        current_row += 1 if going_down else -1

    # Concatenate all rows to get the final string
    return ''.join(rows)
