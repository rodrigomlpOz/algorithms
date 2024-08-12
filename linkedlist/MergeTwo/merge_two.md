### Problem Statement:
Given two sorted linked lists, merge them into one sorted linked list and return the merged list. The merged list should be created by splicing together the nodes of the two given lists.

### Function Signature:
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass
```

### Example Calls:
```python
# Example 1:
# Input: l1 = 1 -> 2 -> 4, l2 = 1 -> 3 -> 4
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
result = Solution().mergeTwoLists(l1, l2)

# Example 2:
# Input: l1 = None, l2 = None
# Output: None

l1 = None
l2 = None
result = Solution().mergeTwoLists(l1, l2)

# Example 3:
# Input: l1 = None, l2 = 0
# Output: 0

l1 = None
l2 = ListNode(0)
result = Solution().mergeTwoLists(l1, l2)
```

### High-Level Solution:
1. **Initialize a Dummy Node:** Create a dummy node that serves as the starting point of the merged linked list. This simplifies the process of appending nodes to the merged list.

2. **Iterate Through Both Lists:** Traverse both linked lists simultaneously. At each step, compare the current node of the two lists and append the smaller value node to the merged list.

3. **Handle Remaining Nodes:** After one of the lists is exhausted, append the remaining nodes of the other list directly to the merged list.

4. **Return the Merged List:** Finally, return the merged linked list, which starts from the node following the dummy node.
