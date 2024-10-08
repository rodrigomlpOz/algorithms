### Problem Statement
You are given a singly linked list `L` and an integer `k`. Your task is to cyclically right shift the linked list by `k` positions. This means that the last `k` nodes of the list will move to the front.

### Problem Definition
Given a singly linked list `L` and an integer `k`, implement a function `cyclically_right_shift_list` that shifts the list to the right by `k` positions and returns the new head of the shifted list.

- **Input:**
  - `L`: The head node of a singly linked list.
  - `k`: An integer representing the number of positions to shift the list.

- **Output:**
  - The head node of the shifted linked list.

### Function Signature
```python
def cyclically_right_shift_list(L: ListNode, k: int) -> ListNode:
   pass
```

### Example
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the node
        self.next = next  # Pointer to the next node in the linked list


def list_to_linkedlist(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linkedlist(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

# Example 1:
L1 = list_to_linkedlist([1, 2, 3, 4, 5])
k1 = 2
result1 = cyclically_right_shift_list(L1, k1)
print("Example 1:")
print_linkedlist(result1)  # Output: 4 -> 5 -> 1 -> 2 -> 3

# Example 2:
L2 = list_to_linkedlist([1, 2, 3, 4, 5])
k2 = 7
result2 = cyclically_right_shift_list(L2, k2)
print("Example 2:")
print_linkedlist(result2)  # Output: 4 -> 5 -> 1 -> 2 -> 3
```

### High-Level Solution
1. **Handle the Edge Case:**
   - If the list is empty (`L is None`), return `None` immediately.

2. **Compute the Length of the List and the Tail Node:**
   - Traverse the list to calculate its length `n` and find the tail node. This step is important to understand how many positions `k` will affect.

3. **Optimize `k`:**
   - Since shifting the list by `n` positions brings the list back to its original configuration, compute `k % n` to optimize the number of shifts. If `k % n == 0`, return the original list.

4. **Form a Cycle:**
   - Link the tail of the list to the head, creating a circular linked list.

5. **Find the New Tail and Head:**
   - The new tail will be located `n - k` steps from the original tail. The new head is the node right after this new tail.

6. **Break the Cycle:**
   - Disconnect the new tail's `next` pointer to break the cycle and complete the shift.

7. **Return the New Head:**
   - Return the `new_head` which is now the head of the shifted list.

### Function Call Example
```python
# Example usage:
# Assuming a helper function to create a linked list from a list and another to print the list.

L = create_linked_list([1, 2, 3, 4, 5])
k = 2
new_head = cyclically_right_shift_list(L, k)
print_linked_list(new_head)  # Output: 4 -> 5 -> 1 -> 2 -> 3
```

### Time Complexity
- **Time Complexity:** O(n), where `n` is the number of nodes in the linked list. This is because we traverse the list to compute its length and then make another traversal to adjust the pointers.

- **Space Complexity:** O(1), as the operation is done in place without requiring additional space except for a few pointers.

This approach ensures that the linked list is shifted efficiently, even when `k` is large compared to the size of the list.
