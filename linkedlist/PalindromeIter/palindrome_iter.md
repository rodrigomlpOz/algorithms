### Problem Statement:
Given a singly linked list, determine if it is a palindrome. A linked list is a palindrome if the sequence of values is the same forward and backward.

### Function Signature:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pass
```

### Example Calls:
```python
# Example 1:
# Input: 1 -> 2
# Output: False

head = ListNode(1)
head.next = ListNode(2)
result = Solution().isPalindrome(head)

# Example 2:
# Input: 1 -> 2 -> 2 -> 1
# Output: True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
result = Solution().isPalindrome(head)
```

### High-Level Solution:
1. **Fast and Slow Pointer Approach:** Use two pointers, `current` and `runner`, where `runner` moves twice as fast as `current`. This allows `current` to reach the midpoint of the linked list when `runner` reaches the end.

2. **Use a Stack to Track the First Half:** As `current` moves forward, push the values onto a stack. By the time `runner` reaches the end of the list, the stack contains the first half of the list values in reverse order.

3. **Skip the Middle Element if Necessary:** If the list has an odd number of elements, skip the middle element since it doesn't affect the palindrome property.

4. **Compare the Second Half with the Stack:** Continue traversing the second half of the list with `current` and pop values from the stack to compare. If all values match, the list is a palindrome.

5. **Return the Result:** If any comparison fails, return `False`; otherwise, return `True` once the list is fully traversed.
