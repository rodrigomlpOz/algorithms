### Problem Statement:
You are given a linked list. Write a function to detect whether the linked list has a cycle in it.

A cycle occurs when a node's `next` pointer points to one of the previous nodes, forming a loop. If there is a cycle, return `True`; otherwise, return `False`.

### Function Definition:
```python
def hasCycle(head: ListNode) -> bool:
    """
    Determines if a linked list has a cycle.

    Args:
    head (ListNode): The head of the linked list.

    Returns:
    bool: True if there is a cycle, False otherwise.
    """
```

### High-Level Approach (Two-pointer or Floyd’s Cycle Detection Algorithm):
To detect a cycle in a linked list, we can use two pointers (often called the **slow** and **fast** pointers):
1. **Slow pointer** moves one step at a time.
2. **Fast pointer** moves two steps at a time.
   
- If there is a cycle, eventually the fast pointer will meet the slow pointer because the fast pointer is moving faster inside the cycle.
- If the fast pointer reaches the end of the list (i.e., encounters `None`), there is no cycle.

### Steps:
1. Initialize two pointers, `slow` and `fast`, both starting at the `head` of the linked list.
2. Move the `slow` pointer by one step and the `fast` pointer by two steps at each iteration.
3. If at any point `slow` and `fast` meet, there is a cycle, so return `True`.
4. If the `fast` pointer reaches the end (`None`), return `False` because there is no cycle.

### Python Code Implementation:


### Example Usage:

```python
# Helper function to create a linked list from a list and introduce a cycle
def createLinkedListWithCycle(values, pos):
    head = ListNode(values[0])
    current = head
    cycle_node = None
    
    # Create the linked list nodes
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current  # Remember the node where the cycle should start
    
    # Introduce the cycle by connecting the last node to the cycle node
    if cycle_node:
        current.next = cycle_node
    
    return head

# Test case 1: Linked list with a cycle
values = [3, 2, 0, -4]
pos = 1  # Cycle starts at node 2
head_with_cycle = createLinkedListWithCycle(values, pos)
print(hasCycle(head_with_cycle))  # Output: True

# Test case 2: Linked list without a cycle
values = [1, 2]
pos = -1  # No cycle
head_no_cycle = createLinkedListWithCycle(values, pos)
print(hasCycle(head_no_cycle))  # Output: False

# Test case 3: Single node without a cycle
single_node = ListNode(1)
print(hasCycle(single_node))  # Output: False
```

### Explanation:
1. **Class Definition (`ListNode`)**: A simple class to represent a node in a singly linked list, with a `val` attribute for the value and a `next` attribute for the next node.
2. **Main Function (`hasCycle`)**:
   - It uses the two-pointer technique to detect a cycle.
   - If the `slow` and `fast` pointers meet, the function returns `True` indicating a cycle.
   - If the `fast` pointer reaches the end of the list (`None`), it returns `False`.
3. **Helper Function (`createLinkedListWithCycle`)**: Creates a linked list and optionally introduces a cycle based on the `pos` argument. If `pos` is `-1`, no cycle is created.

### Time and Space Complexity:
- **Time Complexity**: O(n), where n is the number of nodes in the linked list. In the worst case, we may need to visit every node once.
- **Space Complexity**: O(1), since we are only using two pointers and not any additional space that grows with the input size.

This is a common interview question, testing the understanding of linked list traversal and the two-pointer technique (Floyd’s cycle detection algorithm).