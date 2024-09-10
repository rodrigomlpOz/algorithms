def knapSack(W, wt, val, n):
    """
    A recursive function to solve the 0-1 Knapsack Problem in a forward manner.

    Args:
    W : int : The total capacity of the knapsack.
    wt : list : List of item weights.
    val : list : List of item values corresponding to the weights.
    n : int : The number of items to choose from.

    Returns:
    int : The maximum value that can be obtained with the given capacity.
    """
    # Base cases: if the list of items is empty or no capacity is left
    if n == 0 or W == 0:
        return 0

    # If the weight of the current item is more than the remaining capacity, skip it
    if wt[0] > W:
        return knapSack(W, wt[1:], val[1:], n - 1)
    
    # Otherwise, we have two choices:
    # 1. Take the current item and proceed to the next item with reduced capacity
    # 2. Skip the current item and proceed to the next item with the same capacity
    return max(
        val[0] + knapSack(W - wt[0], wt[1:], val[1:], n - 1),  # Include current item
        knapSack(W, wt[1:], val[1:], n - 1)                   # Skip current item
    )

# Example call
W = 50
wt = [10, 20, 30]
val = [60, 100, 120]
n = len(wt)
print(knapSack(W, wt, val, n))  # Output: 220
