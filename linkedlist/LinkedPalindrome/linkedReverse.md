### Problem Statement
You are given a singly linked list and need to determine if it is a palindrome. A linked list is considered a palindrome if it reads the same backward as forward.

### Problem Definition
Implement a function `isPalindrome` that checks if the linked list is a palindrome. Use helper methods to reverse the second half of the list and compare it with the first half.

- **Input:**
  - `head`: The head node of a singly linked list.

- **Output:**
  - A boolean value indicating whether the linked list is a palindrome.

### Function Signature
```python
def isPalindrome(self, head: ListNode) -> bool:
```

### Helper Functions
1. **`end_of_first_half(head: ListNode) -> ListNode`**
   - Finds the end of the first half of the linked list.
   
2. **`reverse_list(head: ListNode) -> ListNode`**
   - Reverses a linked list.

### Example
```python
# Example 1:
# Input: 1 -> 2 -> 2 -> 1
# Output: True

# Example 2:
# Input: 1 -> 2 -> 3 -> 2 -> 1
# Output: True

# Example 3:
# Input: 1 -> 2 -> 3
# Output: False

### High-Level Solution
1. **Find the End of the First Half:**
   - Use the slow and fast pointer technique to find the end of the first half. The slow pointer moves one step at a time, while the fast pointer moves two steps. When the fast pointer reaches the end, the slow pointer will be at the midpoint.

2. **Reverse the Second Half:**
   - Reverse the second half of the linked list starting from the node after the end of the first half.

3. **Check for Palindrome:**
   - Compare the nodes in the first half of the list with those in the reversed second half. If they all match, the list is a palindrome.

4. **Restore the List:**
   - Reverse the second half again to restore the original list structure.

5. **Return the Result:**
   - Return `True` if all nodes match, otherwise `False`.

```
### Time Complexity
- **Time Complexity:** O(n), where `n` is the number of nodes in the linked list. Each node is visited a constant number of times.

- **Space Complexity:** O(1), as no additional space is used other than a few pointers.
