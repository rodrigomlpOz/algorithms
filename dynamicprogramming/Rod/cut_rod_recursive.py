def cutRod(price, n):
    """
    Recursive function to find the maximum obtainable value by cutting the rod.

    Args:
    price : list : List of prices where price[i] is the price of a rod of length i+1.
    n : int : The length of the rod.

    Returns:
    int : The maximum profit obtainable by cutting the rod into pieces.
    """
    # Base case: If the rod length is 0, no value can be obtained
    if n == 0:
        return 0

    # Initialize the maximum value to a very small number
    max_val = float('-inf')

    # Try all possible cuts from 1 to n
    for i in range(1, n + 1):
        # Recursively find the maximum value by including a piece of length i
        # and solving for the remaining rod of length n-i
        max_val = max(max_val, price[i-1] + cutRod(price, n - i))

    return max_val
