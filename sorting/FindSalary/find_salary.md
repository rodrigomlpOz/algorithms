### Problem Statement

Given a list of current salaries and a target payroll budget, determine the salary cap (a uniform salary for all employees) such that the total payroll equals the target budget. If the cap cannot be determined because the target is smaller than the sum of the minimum salaries, return `-1.0`.

### Functional Requirements

1. **Input**:
    - `target_payroll` (float): The desired total payroll.
    - `current_salaries` (list of floats): The current salaries of all employees.

2. **Output**:
    - A float representing the salary cap or `-1.0` if the target payroll cannot be achieved.

3. **Constraints**:
    - If the payroll cannot be met without reducing at least some salaries, determine the minimum salary cap to reach the target.

### Function Signature

```python
def find_salary_cap(target_payroll: float, current_salaries: list[float]) -> float:
```

### Function Calls

```python
# Example 1: 
target_payroll = 210
current_salaries = [90, 30, 100, 40, 20]
cap = find_salary_cap(target_payroll, current_salaries)
print(cap)  # Output: 60.0

# Example 2: 
target_payroll = 400
current_salaries = [90, 30, 100, 40, 20]
cap = find_salary_cap(target_payroll, current_salaries)
print(cap)  # Output: -1.0 (Target cannot be met as is)

# Example 3: 
target_payroll = 130
current_salaries = [30, 20, 50]
cap = find_salary_cap(target_payroll, current_salaries)
print(cap)  # Output: 43.33 (approximately)
```

### High-Level Solution

1. **Sort the Salaries**: Start by sorting the salaries in ascending order.

2. **Iterate through the Sorted Salaries**:
    - For each salary, determine whether capping the salaries of all higher-paid employees at this level will meet or exceed the target payroll.
    - If it does, calculate the exact cap by distributing the remaining payroll budget equally among all employees that would be capped at this level.

3. **Calculate the Cap**:
    - The cap is calculated by dividing the remaining payroll budget by the number of employees whose salaries would need to be capped.

4. **Edge Cases**:
    - If the total sum of the current salaries is less than the target, return `-1.0`.
    - Handle scenarios where the cap would exceed all salaries.

### Explanation

The algorithm works by progressively analyzing each potential cap (starting from the lowest salary) and determining if it allows achieving the target payroll. It does this by computing the unadjusted sum of salaries below the current potential cap and checking if capping the remaining salaries can reach the desired target.
