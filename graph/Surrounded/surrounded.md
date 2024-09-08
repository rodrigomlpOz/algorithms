### Problem: Surrounded Regions (Leetcode 130)

The task is to modify a 2D board of `'X'` and `'O'` such that all `'O'` regions completely surrounded by `'X'` are flipped to `'X'`. Any `'O'` connected to the board's boundary should not be flipped.

### High-Level Solution:

1. **Identify Boundary-Connected Regions**:
   - The first step is to identify the `'O'` regions that are connected to the boundary of the board. These boundary-connected `'O'` cells cannot be flipped because they are not fully surrounded by `'X'`.

2. **Mark Boundary-Connected `'O'` Cells**:
   - Traverse the first and last rows, and first and last columns of the grid. Whenever a boundary cell contains `'O'`, perform a DFS or BFS to mark all `'O'` cells connected to this boundary `'O'`. Mark these cells temporarily (e.g., with a special character like `'S'`) so that they won’t be flipped.

3. **Flip Interior `'O'` Cells**:
   - After marking all the boundary-connected `'O'` cells, traverse the entire board. Any remaining `'O'` cells that were not marked during the DFS/BFS are interior cells surrounded by `'X'`, so they should be flipped to `'X'`.

4. **Restore Marked Cells**:
   - After flipping the interior `'O'` cells, the boundary-connected `'O'` cells that were marked as `'S'` should be restored to `'O'` since they must remain unchanged.

### Steps to Solve:

1. **Step 1**: Traverse the boundary (first and last rows, first and last columns). For each `'O'` found on the boundary, start a DFS/BFS to mark all connected `'O'` cells.
   
2. **Step 2**: Mark all `'O'` cells connected to the boundary using a temporary character (e.g., `'S'`).

3. **Step 3**: Traverse the entire board. Flip any remaining unmarked `'O'` to `'X'`.

4. **Step 4**: Traverse the board again and revert the marked `'S'` cells back to `'O'`.

### Time Complexity:
- **Time Complexity**: O(m * n), where `m` is the number of rows and `n` is the number of columns in the board. Each cell is processed at most twice (once for marking and once for flipping or restoring).

### Space Complexity:
- **Space Complexity**: O(m * n) in the worst case, due to the recursion stack in DFS or the queue in BFS.

By marking the boundary-connected `'O'` regions first and then processing the entire board, this approach ensures that only the surrounded regions are flipped.
