def editDistance(str1, str2, m, n):
    """
    A recursive function to find the minimum number of operations required
    to convert str1 into str2.

    Args:
    str1 : str : The first string.
    str2 : str : The second string.
    m : int : The length of the first string.
    n : int : The length of the second string.

    Returns:
    int : The minimum number of edit operations required to convert str1 to str2.
    """
    # Base case: If str1 is empty, we need to insert all characters of str2
    if m == 0:
        return n

    # Base case: If str2 is empty, we need to delete all characters of str1
    if n == 0:
        return m

    # If the last characters are the same, no operation is needed
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)

    # If the last characters are different, consider all three operations
    return min(
        editDistance(str1, str2, m, n - 1) + 1,      # Insert
        editDistance(str1, str2, m - 1, n) + 1,      # Delete
        editDistance(str1, str2, m - 1, n - 1) + 1   # Substitute
    )
