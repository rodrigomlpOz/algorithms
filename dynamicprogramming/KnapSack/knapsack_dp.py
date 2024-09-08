def knapSack(W, wt, val, n):
    """
    Solves the 0-1 Knapsack problem using dynamic programming.
    
    Args:
    W : int : The capacity of the knapsack.
    wt : list : List of item weights.
    val : list : List of item values.
    n : int : The number of items.
    
    Returns:
    int : The maximum value that can be achieved with the given items and knapsack capacity.
    """
    
    # 1. Define the DP Table
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # 2. Initialize the DP Table
    # (This is done implicitly by setting the first row and column to 0)
    # No explicit initialization needed as Python defaults to 0 in the list comprehensions.

    # 3. Fill the DP Table using the recurrence relation
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0  # Base case: no items or zero capacity
            elif wt[i-1] <= w:
                # Option 1: Include the item (val[i-1] + K[i-1][w-wt[i-1]])
                # Option 2: Exclude the item (K[i-1][w])
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                # Cannot include the item, carry over the value without the item
                K[i][w] = K[i-1][w]

    # 4. Return the result stored in K[n][W]
    return K[n][W]

# Driver code to test the function
val = [60, 100, 120]  # List of item values
wt = [10, 20, 30]     # List of item weights
W = 50                # Maximum capacity of the knapsack
n = len(val)          # Number of items

# Calling the knapSack function and printing the result
print(knapSack(W, wt, val, n))
