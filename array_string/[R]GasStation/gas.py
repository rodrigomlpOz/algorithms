def canCompleteCircuit(gas, cost):
    total_gas, total_cost = 0, 0
    tank_balance, start_station = 0, 0
    
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank_balance += gas[i] - cost[i]
        
        # If tank balance is negative, can't proceed from current start
        if tank_balance < 0:
            # Set next station as the starting station
            start_station = i + 1
            tank_balance = 0  # Reset the tank balance
    
    # Check if total gas is enough to cover the total cost
    return start_station if total_gas >= total_cost else -1

# Test case
gas = [1, 2, 3, 4]
cost = [2, 2, 4, 1]
print(canCompleteCircuit(gas, cost))  # Output: 3
