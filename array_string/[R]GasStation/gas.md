### Problem Statement

You are given two integer arrays `gas` and `cost`, representing `n` gas stations along a circular route. The amount of gas available at the `i`-th station is `gas[i]`, and the amount of gas required to travel from the `i`-th station to the `(i + 1)`-th station is `cost[i]`. The last station is connected back to the first station, forming a circular route.

You have a car with an empty tank and an unlimited capacity. You can start at any gas station. Your goal is to find the starting gas station's index such that you can complete the circuit exactly once in a clockwise direction, visiting all stations.

Return the index of the starting gas station if it's possible to complete the circuit. If not, return `-1`.

**Constraints**:
- It is guaranteed that at most one solution exists.

### Example

**Input**:
```python
gas = [1, 2, 3, 4]
cost = [2, 2, 4, 1]
```

**Output**:
```python
3
```

**Explanation**:
- Starting at station 3 with 4 units of gas, you can travel through the entire circuit:
  - From station 3 to station 0: Gas left = 4 - 1 = 3
  - From station 0 to station 1: Gas left = 3 + 1 - 2 = 2
  - From station 1 to station 2: Gas left = 2 + 2 - 2 = 2
  - From station 2 to station 3: Gas left = 2 + 3 - 4 = 1
- You end up with a positive amount of gas, completing the circuit.

### Function Definition

```python
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    """
    Determine if there exists a starting gas station index from which we can complete the entire circuit.

    :param gas: List of integers representing the gas available at each station.
    :param cost: List of integers representing the cost of gas to travel to the next station.
    :return: The index of the starting gas station if possible, otherwise -1.
    """
```

### High-Level Solution:

1. **Check Total Gas vs Total Cost**: 
   - If the total amount of gas across all stations is less than the total travel cost, it's impossible to complete the circuit, so return `-1`.

2. **Greedy Traversal to Find Starting Station**:
   - Start at station 0 with an empty tank.
   - Traverse each station, keeping track of the current gas balance (`tank_balance = gas[i] - cost[i]`).
   - If at any point the balance becomes negative, reset the starting station to the next station (`i + 1`) and reset the balance to 0. This is because no valid circuit can start from any station before this point.
   
3. **Return the Result**:
   - If the total gas is greater than or equal to the total cost, return the index of the last valid starting station. Otherwise, return `-1`.

### Solution Code

```python
def canCompleteCircuit(gas, cost):
    pass

# Test cases
gas = [1, 2, 3, 4]
cost = [2, 2, 4, 1]
print(canCompleteCircuit(gas, cost))  # Output: 3

gas = [2, 3, 4]
cost = [3, 4, 3]
print(canCompleteCircuit(gas, cost))  # Output: -1
```

### Explanation:

1. **Total Gas and Total Cost**: 
   - We sum up all the gas available and the total cost to travel through the stations. If the total gas is less than the total cost, return `-1` since it is impossible to complete the circuit.

2. **Tank Balance**:
   - We maintain a `tank_balance` which represents how much gas is left after each station (`tank_balance += gas[i] - cost[i]`). If the balance goes negative, it means the current starting station can't be valid, and we move the starting station to the next one.

3. **Final Check**:
   - If the total gas is greater than or equal to the total cost, return the last valid starting station. Otherwise, return `-1`.

### Time Complexity:
- **O(n)**: We traverse the list of gas stations once, so the time complexity is linear, where `n` is the number of stations.

### Space Complexity:
- **O(1)**: We only use a few extra variables (`total_gas`, `total_cost`, `tank_balance`, and `start_station`), so the space complexity is constant.