### Problem Statement: Insert Delete GetRandom O(1)

**Problem Description:**

Implement the `RandomizedSet` class:

- `bool insert(int val)`:
  - Inserts an item `val` into the set if not present. Returns `True` if the item was not present, `False` otherwise.
- `bool remove(int val)`:
  - Removes an item `val` from the set if present. Returns `True` if the item was present, `False` otherwise.
- `int getRandom()`:
  - Returns a random element from the current set of elements. Each element must have the same probability of being returned.

**Constraints:**

- Implement the functions such that each function works in average O(1) time complexity.

### High-Level Approach

1. **Data Structures:**
   - Use a list to store the elements. This allows for O(1) time complexity for `getRandom()` by leveraging Python’s `random.choice`.
   - Use a dictionary to map the values to their indices in the list. This allows for O(1) time complexity for both `insert` and `remove` operations.

2. **Insert Operation:**
   - Check if the value already exists in the dictionary.
   - If it does not exist, append the value to the list and record its index in the dictionary.
   - If it exists, return `False`.

3. **Remove Operation:**
   - Check if the value exists in the dictionary.
   - If it exists, find its index in the list. Swap the element with the last element in the list.
   - Update the dictionary to reflect the new index of the swapped element.
   - Remove the last element from the list and delete the value from the dictionary.
   - If it does not exist, return `False`.

4. **Get Random Operation:**
   - Use `random.choice` to return a random element from the list.

### Implementation

Here’s how you can implement the `RandomizedSet` class in Python:
