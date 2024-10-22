### Problem Statement:
You are given a list of tuples, where each tuple contains a first name and a last name. The goal is to remove duplicate entries based on the first name, keeping only the first occurrence (in alphabetical order) of each first name. The order of the output list should be determined by the alphabetical order of first names.

### Functional Definition:
1. **Function Name:** `remove_first_name_duplicates`
2. **Input Parameters:**
   - `names` (List of tuples): A list of tuples where each tuple contains a `first name` and a `last name`.
   
3. **Output:**
   - A list of tuples where each first name appears only once. If there are duplicates, only the first occurrence in alphabetical order of first names is retained.

4. **Example Call:**
   ```python
   def remove_first_name_duplicates(names):
    pass

   names = [("Ian", "Botham"), ("David", "Gower"), ("Ian", "Bell"), ("Ian", "Chappell")]
   result = remove_first_name_duplicates(names)
   # Output: [("David", "Gower"), ("Ian", "Botham")]
   ```

### High-Level Solution:
1. **Sorting:**
   - Sort the list of tuples based on the first name to ensure that the first occurrence of each name is in alphabetical order.
   
2. **Iterating and Filtering:**
   - Iterate through the sorted list and keep track of the first name as you go.
   - Append each tuple to the result list `ans` only if its first name hasn't been encountered before.

3. **Return Result:**
   - The result list `ans` will contain tuples where each first name is unique, keeping only the first occurrence of each name.

### Python Implementation:

```python
def remove_first_name_duplicates(names):
    # Sort the names based on the first name
    sorted_names = sorted(names, key=lambda x: x[0])
    ans = []
    
    for i in range(len(sorted_names)):
        # Add the name to the result if it's the first occurrence of that first name
        if i == 0 or sorted_names[i-1][0] != sorted_names[i][0]:
            ans.append(sorted_names[i])
    
    return ans

# Example usage
names = [("Ian", "Botham"), ("David", "Gower"), ("Ian", "Bell"), ("Ian", "Chappell")]
result = remove_first_name_duplicates(names)
print(result)  # Output: [("David", "Gower"), ("Ian", "Botham")]
```

### Explanation:
- **Sorting by First Name:** The function begins by sorting the list of names by the first name, ensuring that duplicates are placed next to each other.
- **Avoiding Duplicates:** The loop iterates through the sorted list, appending a tuple to the result list only if its first name hasn't been seen before.
- **Final Output:** The resulting list contains unique first names, with only the first occurrence (based on alphabetical order) retained.

This approach ensures that the function efficiently removes duplicates based on the first name while preserving the first occurrence of each name in alphabetical order.
