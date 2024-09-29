### Problem Statement:
Given the head of a singly linked list, sort the list in ascending order and return the sorted list. The goal is to implement an efficient sorting algorithm that works in O(n log n) time complexity and uses constant space (O(1)) for the list nodes.

### Function Signature:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def sortList(self, head: ListNode) -> ListNode:
    pass
```

### Example Calls:
```python
# Example 1:
# Input: 4 -> 2 -> 1 -> 3
# Output: 1 -> 2 -> 3 -> 4

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
result = sortList(head)

# Example 2:
# Input: -1 -> 5 -> 3 -> 4 -> 0
# Output: -1 -> 0 -> 3 -> 4 -> 5

head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)
result = sortList(head)
```

### High-Level Solution:
1. **Base Case:** If the list is empty or contains a single node, it is already sorted, so return the head.

2. **Find the Middle Node:** Use the fast and slow pointer technique to find the middle of the linked list. This helps in dividing the list into two halves.

3. **Recursive Sorting:** Recursively sort both halves of the linked list. This approach ensures that each half is independently sorted.

4. **Merge Sorted Halves:** Merge the two sorted halves back together using a helper function. This function combines the two halves into a single sorted linked list.

5. **Return the Sorted List:** After merging, the fully sorted list is returned as the result.

This approach uses the **merge sort** algorithm, which is well-suited for linked lists due to its O(n log n) time complexity and the ability to work in-place without requiring additional memory allocation for list nodes.
