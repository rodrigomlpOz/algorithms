### Problem Statement

You are given a singly linked list and need to determine if it is a palindrome. A linked list is considered a palindrome if it reads the same backward as forward.

### Problem Definition

Implement a function `isPalindrome` that checks if the linked list is a palindrome. Use helper methods to reverse the second half of the list and compare it with the first half.

### Function Signature
```python
def isPalindrome(head: ListNode) -> bool:
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
```

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

### Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to reverse a linked list
def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Helper function to find the end of the first half
def end_of_first_half(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

# Main function to check if the list is a palindrome
def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True  # Empty list or single element is a palindrome

    # Step 1: Find the end of the first half
    first_half_end = end_of_first_half(head)
    
    # Step 2: Reverse the second half of the list
    second_half_start = reverse_list(first_half_end.next)

    # Step 3: Compare the first half and the reversed second half
    first_position = head
    second_position = second_half_start
    palindrome = True
    while palindrome and second_position:
        if first_position.val != second_position.val:
            palindrome = False
        first_position = first_position.next
        second_position = second_position.next

    # Step 4: Restore the list
    first_half_end.next = reverse_list(second_half_start)

    return palindrome
```

### Example Test Cases

```python
# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Test Case 1: Palindrome List
head1 = create_linked_list([1, 2, 2, 1])
print("Original List 1:")
print_linked_list(head1)
print("Is Palindrome:", isPalindrome(head1))
print("Restored List 1:")
print_linked_list(head1)

# Test Case 2: Palindrome List
head2 = create_linked_list([1, 2, 3, 2, 1])
print("\nOriginal List 2:")
print_linked_list(head2)
print("Is Palindrome:", isPalindrome(head2))
print("Restored List 2:")
print_linked_list(head2)

# Test Case 3: Not a Palindrome
head3 = create_linked_list([1, 2, 3])
print("\nOriginal List 3:")
print_linked_list(head3)
print("Is Palindrome:", isPalindrome(head3))
```

### Time Complexity
- **O(n)** where `n` is the number of nodes in the list. We pass through the list three times: once to find the middle, once to reverse, and once to restore.

### Space Complexity
- **O(1)**, because we use only a few pointers and do not require additional space proportional to the input size.
