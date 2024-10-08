### Problem Statement
You are given a singly linked list, represented by the head node `L`, and an integer `k`. Your task is to remove the k-th last node from the linked list. It is guaranteed that the linked list has at least `k` nodes.

### Problem Definition
Given a singly linked list `L` and an integer `k`, implement a function `remove_kth_last` that removes the k-th last node from the linked list and returns the head of the modified linked list.

- **Input:**
  - `L`: The head node of a singly linked list.
  - `k`: An integer representing the position from the end of the list of the node that needs to be removed.

- **Output:**
  - The head node of the modified linked list after removing the k-th last node.

### Function Signature
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    """
    Removes the k-th last node from the list and returns the modified list.
    """
    pass

# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(head: ListNode):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

# Test case 1
lst = [1, 2, 3, 4, 5]
k = 2
L = create_linked_list(lst)
print("Original List:")
print_linked_list(L)
print(f"After removing {k}-th last node:")
L = remove_kth_last(L, k)
print_linked_list(L)

# Test case 2
lst = [10, 20, 30, 40, 50]
k = 1
L = create_linked_list(lst)
print("\nOriginal List:")
print_linked_list(L)
print(f"After removing {k}-th last node:")
L = remove_kth_last(L, k)
print_linked_list(L)

# Test case 3
lst = [1, 2]
k = 2
L = create_linked_list(lst)
print("\nOriginal List:")
print_linked_list(L)
print(f"After removing {k}-th last node:")
L = remove_kth_last(L, k)
print_linked_list(L)

```

### Example
```python
# Example 1:
# Input: L = [1 -> 2 -> 3 -> 4 -> 5], k = 2
# Output: [1 -> 2 -> 3 -> 5]

# Example 2:
# Input: L = [1 -> 2 -> 3 -> 4 -> 5], k = 5
# Output: [2 -> 3 -> 4 -> 5]
```

### High-Level Solution
1. **Initialize a Dummy Node:**
   - Create a `dummy_head` node that points to the head of the linked list. This is useful to handle edge cases where the head of the list might be removed.

2. **Advance the First Pointer:**
   - Start by advancing the `first` pointer `k` nodes into the list. This ensures that when the `first` pointer reaches the end of the list, the `second` pointer will be exactly `k` nodes behind it.

3. **Advance Both Pointers:**
   - Move both `first` and `second` pointers simultaneously until `first` reaches the end of the list. After this, the `second` pointer will be pointing to the node just before the k-th last node.

4. **Remove the k-th Last Node:**
   - Adjust the `next` pointer of the `second` node to skip the k-th last node, effectively removing it from the list.

5. **Return the Modified List:**
   - Return the modified list starting from `dummy_head.next`, which ensures that the correct head is returned even if the original head was removed.

This approach ensures that the removal is done in a single pass with O(n) time complexity and O(1) space complexity.
