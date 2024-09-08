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
Here's an expanded high-level description of the solution:

### High-Level Solution Description:
The 0-1 Knapsack problem is a combinatorial optimization problem. The goal is to select a subset of items such that the total weight does not exceed the given knapsack capacity, and the total value is maximized.

The problem can be approached recursively:

1. **Base Case:**
   - If there are no items left to consider (`n == 0`), or the capacity of the knapsack is exhausted (`W == 0`), the maximum value is `0` since no more items can be included.

2. **Recursive Decision:**
   - For each item `i`, there are two possibilities:
     - **Exclude the item**: Simply skip this item and move to the next. The maximum value would then depend on the remaining items (`n-1`) and the same knapsack capacity (`W`).
     - **Include the item**: If the weight of the item is less than or equal to the remaining knapsack capacity, you can include this item. The remaining capacity is reduced by the weight of this item (`W - wt[i-1]`), and you add the value of this item to the total value.
     
3. **Optimization:**
   - For each item, you compute the maximum value by considering both including and excluding the item. The optimal solution is the one that maximizes the total value.
   - You recursively call the function to check all possible combinations and return the maximum of the two scenarios (including or excluding the current item).

4. **Key Idea:**
   - The recursive process explores all possible combinations of including and excluding items.
   - The solution is "naive" because it recalculates the result for the same subproblems multiple times. This leads to an exponential time complexity of `O(2^n)` since there are two decisions (include or exclude) for each item.

5. **Outputs:**
   - The final result of the function will be the maximum total value that can be achieved by selecting a subset of items while staying within the weight limit `W`.

### Example Walkthrough:
For example, given the items:
- Values: `[60, 100, 120]`
- Weights: `[10, 20, 30]`
- Knapsack capacity: `W = 50`

The function will:
1. Consider whether to include or exclude the third item (weight 30, value 120).
2. If excluded, the problem reduces to the first two items with the same capacity (`W = 50`).
3. If included, the capacity reduces to `W = 20`, and the function solves for the first two items with the reduced capacity.
4. The maximum value between these two options is returned.

This process continues recursively for all items, eventually finding the optimal combination.

Let me know if this helps or if you need further clarification!
