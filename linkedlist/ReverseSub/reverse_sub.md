### Problem Statement
You are given a singly linked list and two integers `m` and `n`, where `1 <= m <= n <= length of the list`. Your task is to reverse the nodes of the list from position `m` to `n` and return the head of the modified linked list.

### Problem Definition
Given the head of a singly linked list, and two integers `m` and `n`, implement a function `reverseBetween` that reverses the nodes from position `m` to `n` in the linked list.

- **Input:**
  - `head`: The head node of a singly linked list.
  - `m`: An integer representing the start position of the sublist to reverse.
  - `n`: An integer representing the end position of the sublist to reverse.

- **Output:**
  - The head node of the modified linked list after reversing the sublist.

### Function Signature
```python
def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
```

### Example
```python
# Example 1:
# Input: head = [1 -> 2 -> 3 -> 4 -> 5], m = 2, n = 4
# Output: [1 -> 4 -> 3 -> 2 -> 5]

# Example 2:
# Input: head = [1 -> 2 -> 3], m = 1, n = 3
# Output: [3 -> 2 -> 1]
```

### High-Level Solution
1. **Initialize Dummy and Sublist Head:**
   - Create a `dummy_head` node that points to the head of the linked list. This helps in handling cases where the head of the list might be part of the reversed sublist.
   - Use `sublist_head` to navigate to the node just before the start of the sublist to be reversed.

2. **Move to the Start of the Sublist:**
   - Advance `sublist_head` to the node just before the `m`-th node, as this will be the point where the reversal starts.

3. **Reverse the Sublist:**
   - Initialize `sublist_iter` to the `m`-th node and iteratively reverse the pointers between the `m`-th and `n`-th nodes. This is done by temporarily storing the next node and updating pointers to achieve the reversal.

4. **Return the Modified List:**
   - After the sublist has been reversed, return the modified list starting from `dummy_head.next`, which points to the correct head of the list.

### Explanation of the Reversal Process
- **Reversing the Sublist:**
  - The key idea is to iteratively extract the next node in the sublist and insert it at the beginning of the reversed portion. This process effectively moves each node in the sublist to the front of the sublist head, thus reversing the order.

### Time Complexity
- **Time Complexity:** O(n), where `n` is the number of nodes in the linked list. Each node is visited at most once.

- **Space Complexity:** O(1), as the reversal is performed in place without using any extra space apart from a few pointers.

### Example Function Call
```python
# Example usage:
sol = Solution()
head = create_linked_list([1, 2, 3, 4, 5])
new_head = sol.reverseBetween(head, 2, 4)
print_linked_list(new_head)  # Output: 1 -> 4 -> 3 -> 2 -> 5
```

This approach ensures that the specified portion of the linked list is reversed efficiently, with careful handling of edge cases where the head is part of the sublist.
