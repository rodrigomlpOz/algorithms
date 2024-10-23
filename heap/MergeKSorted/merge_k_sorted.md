### Problem Statement:
You are given an array of `k` sorted linked lists. Each linked list is sorted in ascending order. The goal is to merge all these linked lists into a single sorted linked list and return its head.

### Function Definition:
```python
def mergeKLists(lists: list[ListNode]) -> ListNode:
    """
    Merges an array of k sorted linked lists into a single sorted linked list.
    
    Args:
    lists (list[ListNode]): A list containing the head nodes of k sorted linked lists.
    
    Returns:
    ListNode: The head node of the merged sorted linked list.
    """
```

### Function Calls:
```python
# Example 1: Merging three sorted linked lists
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

merged_head = mergeKLists([list1, list2, list3])
# The expected output linked list: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

# Example 2: Merging an empty list
merged_head = mergeKLists([])
# The expected output linked list: None (empty list)

# Example 3: Merging a list of one empty linked list
merged_head = mergeKLists([None])
# The expected output linked list: None (empty list)
```

### High-Level Solution:
1. **Use a Min-Heap to Maintain the Smallest Node from Each List:**
   - A min-heap (priority queue) is used to keep track of the smallest node among the current heads of all the linked lists.
   - Each entry in the heap is a tuple `(node value, index of the list, node)`.

2. **Initialize the Heap with the First Node of Each List:**
   - Iterate through the input list of linked lists, and push the head of each non-empty list into the heap.

3. **Build the Merged Linked List:**
   - Use a dummy node to simplify the construction of the resulting linked list.
   - Continuously pop the smallest node from the heap, append it to the merged list, and push the next node from the same list (if it exists) into the heap.

4. **Return the Head of the Merged Linked List:**
   - The dummy node's `next` pointer will point to the head of the merged linked list.

This approach ensures an efficient merge operation by maintaining a heap of size `k`, where `k` is the number of linked lists. The overall time complexity is \(O(N \log k)\), where \(N\) is the total number of nodes across all lists.
