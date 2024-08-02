### Problem Statement

Given a singly linked list, group all odd nodes together followed by the even nodes. Here, we are talking about the node number and not the value in the nodes. The program should preserve the relative order of the nodes within each group. The first node is considered odd, the second node even, and so on.

### Function Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def even_odd_merge(L: ListNode) -> ListNode:
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
L = create_linked_list([1, 2, 3, 4, 5])
result = even_odd_merge(L)
print(linked_list_to_list(result))  # Output: [1, 3, 5, 2, 4]
```

### High-Level Solution

1. **Edge Case Handling**: If the linked list is empty, return the list as it is.

2. **Initialize Dummy Nodes and Pointers**: Create two dummy nodes (`even_dummy_head` and `odd_dummy_head`) to simplify the handling of even and odd lists. Use an array `tails` to keep track of the tails of the even and odd lists. Initialize a variable `turn` to alternate between even and odd.

3. **Iterate Through the List**: Traverse the input list, attaching nodes alternately to the even and odd lists using the `tails` pointers. Use the `turn` variable to decide whether the current node should go into the even or odd list.

4. **Merge the Lists**: Once the end of the input list is reached, set the `next` pointer of the last node in the odd list to `None` to terminate the list. Then, link the last node in the even list to the head of the odd list.

5. **Return the Result**: Return the head of the merged list, which starts from the node next to `even_dummy_head`.

This approach ensures that all even-indexed nodes are grouped together followed by all odd-indexed nodes, maintaining the original relative order within each group.
