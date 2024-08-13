### Problem Statement
You are given a sorted singly linked list represented by the head node `L`. Your task is to remove all duplicate nodes from the list so that each element appears only once. The linked list should be modified in place.

### Problem Definition
Given a sorted singly linked list `L`, implement a function `remove_duplicates` that removes all duplicate nodes from the list and returns the head of the modified linked list.

- **Input:**
  - `L`: The head node of a sorted singly linked list.

- **Output:**
  - The head node of the modified linked list with duplicates removed.

### Function Signature
```python
def remove_duplicates(L: ListNode) -> Optional[ListNode]:
```

### Example
```python
# Example 1:
# Input: L = [1 -> 1 -> 2 -> 3 -> 3]
# Output: [1 -> 2 -> 3]

# Example 2:
# Input: L = [1 -> 2 -> 3 -> 4 -> 5]
# Output: [1 -> 2 -> 3 -> 4 -> 5]
```

### High-Level Solution
1. **Initialize the Iterator:**
   - Start with an iterator `it` pointing to the head of the linked list.

2. **Traverse the List:**
   - While `it` is not `None`, check if the next node has the same value as the current node (`it`). If it does, continue moving a secondary pointer (`next_distinct`) until a node with a different value is found or the end of the list is reached.

3. **Remove Duplicates:**
   - Set the `next` pointer of the current node (`it`) to the `next_distinct` node, effectively skipping all the duplicate nodes.

4. **Move the Iterator:**
   - Move the iterator to the `next_distinct` node and continue the process until the end of the list is reached.

5. **Return the Modified List:**
   - Return the modified list starting from the original head, now with all duplicates removed.

This approach ensures that all duplicate nodes are removed in a single pass with O(n) time complexity and O(1) space complexity, as it modifies the list in place.

### Function Call Example
```python
# Example usage:
# Assuming a helper function to create a linked list from a list and another to print the list.

L = create_linked_list([1, 1, 2, 3, 3])
L = remove_duplicates(L)
print_linked_list(L)  # Output: 1 -> 2 -> 3
```
