### Problem Statement:

Given the head of a singly linked list, reorder the list so that the nodes are arranged in the following order:
- First, take the node from the beginning of the list.
- Then, take the node from the end of the list.
- Next, take the second node from the beginning.
- Then, take the second-to-last node from the end.
- Continue alternating nodes from the start and end until all nodes are reordered.

You need to perform this reordering **in-place** without modifying the values of the nodes.

### Function Definition:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    """
    Reorders the list as described in the problem.
    This function modifies the linked list in-place and returns nothing.
    """
```

### Example:

**Input:**
```python
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
```

**Function Call:**
```python
reorderList(head)
```

**Output:**
```python
# The linked list is modified in place to become:
# 1 -> 4 -> 2 -> 3
```

### High-Level Solution:

The reordering can be broken down into three main steps:

1. **Find the middle of the linked list**:
   - Use the **slow and fast pointer technique** to find the middle of the list. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps at a time. When `fast` reaches the end, `slow` will point to the middle of the list.

2. **Reverse the second half of the list**:
   - After finding the middle, reverse the second half of the list starting from the middle node to the end. This allows you to merge nodes from the start and end of the list in alternating order.

3. **Merge the two halves**:
   - Now, merge the two halves of the list by alternating nodes from the first half and the reversed second half. Start with the first node from the first half, then take the first node from the reversed half, and continue until all nodes are merged.

This approach ensures that the list is reordered in-place without needing any additional data structures.

### Steps Outline:

1. **Finding the middle**: The slow pointer will eventually reach the middle of the list.
2. **Reversing the second half**: Reverse the second half of the list to easily access nodes from the end.
3. **Merging the two halves**: Start alternating nodes from the beginning and reversed second half, modifying pointers accordingly.

This high-level solution runs in \(O(n)\) time, where \(n\) is the number of nodes in the linked list, and uses \(O(1)\) extra space.
