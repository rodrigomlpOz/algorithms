### Problem Statement

Given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Function Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_list(L1: ListNode, L2: ListNode) -> ListNode:
    # Function implementation goes here
    pass
```

### Function Calls

```python
# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

# Helper function to convert linked list to a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
L1 = create_linked_list([2, 4, 3])
L2 = create_linked_list([5, 6, 4])
result = add_list(L1, L2)
print(linked_list_to_list(result))  # Output: [7, 0, 8]
```

### High-Level Solution

1. **Initialize Pointers and Variables**: Create a dummy head node to simplify handling the result list, a pointer for iteration (`place_iter`), and a variable to manage carry-over (`carry`).

2. **Iterate Through Lists**: Loop through both linked lists until all nodes have been processed and there is no remaining carry.

3. **Calculate Sum and Carry**: For each node, compute the sum of the corresponding nodes' values from both lists, including the carry from the previous operation. Update the carry for the next digit.

4. **Create New Nodes**: Create new nodes for the resulting linked list with the digit resulting from the sum modulo 10. Move the iteration pointers forward.

5. **Return Result**: Return the next node of the dummy head, which points to the start of the resultant linked list.

This high-level approach ensures that the algorithm efficiently adds the two numbers represented by the linked lists and manages any carry-over appropriately.
