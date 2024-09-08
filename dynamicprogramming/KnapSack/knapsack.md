Here's the breakdown with only the function calls and the problem details, excluding the solution:

### Problem Statement:
Given a list of items with specific weights and values, and a knapsack with a fixed weight capacity, find the maximum total value that can be placed in the knapsack without exceeding the weight limit. The 0-1 knapsack problem restricts items to either being fully included or excluded (no partial items allowed).

### Function Definition:
```python
def knapSack(W, wt, val, n):
    """
    A recursive function to solve the 0-1 Knapsack Problem.

    Args:
    W : int : The total capacity of the knapsack.
    wt : list : List of item weights.
    val : list : List of item values corresponding to the weights.
    n : int : The number of items to choose from.

    Returns:
    int : The maximum value that can be obtained with the given capacity.
    """
    # Function body implementation will go here
    pass
```

### Function Calls:
```python
# List of item values and weights
val = [60, 100, 120]
wt = [10, 20, 30]

# Capacity of the knapsack
W = 50

# Number of items
n = len(val)

# Calling the function to calculate the maximum value
print(knapSack(W, wt, val, n))
```

### High-Level Description:
1. **Input:**
   - `W`: Maximum weight capacity of the knapsack.
   - `wt`: A list containing the weights of the available items.
   - `val`: A list containing the values corresponding to each item.
   - `n`: Total number of available items.
   
2. **Output:**
   - The maximum value that can be obtained without exceeding the weight limit of the knapsack.

3. **Objective:**
   - Determine the optimal combination of items to include in the knapsack, such that the total value is maximized, and the total weight does not exceed `W`. Each item can either be included or excluded.

Let me know if you need any more details!
