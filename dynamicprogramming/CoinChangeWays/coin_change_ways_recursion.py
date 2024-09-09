def coin_change_ways_recursive(amount, coins):
    """
    Recursive function to calculate the number of ways to make the amount using the given coins.
    
    Args:
    amount: int - The target amount.
    coins: List[int] - A list of available coin denominations.
    
    Returns:
    int - The number of ways to make the target amount using the coins.
    """
    # Base cases
    if amount == 0:
        return 1  # Found a valid combination
    if amount < 0 or len(coins) == 0:
        return 0  # No valid combination

    # Include the current coin and exclude the current coin
    return coin_change_ways_recursive(amount - coins[-1], coins) + coin_change_ways_recursive(amount, coins[:-1])

# Example usage
amount = 5
coins = [1, 2, 5]
print(coin_change_ways_recursive(amount, coins))  # Output: 4
