### Problem: Course Schedule (Leetcode 207)

We need to determine if it is possible to complete all courses given their prerequisites. This problem can be represented as a **directed graph** where:
- Each course is a node.
- A directed edge from course `A` to course `B` means course `A` is a prerequisite for course `B`.

The problem reduces to detecting **cycles** in the graph. If a cycle exists, it’s impossible to complete all courses.

### High-Level Solution:

1. **Graph Representation**:
   - Build a graph where each course is a node, and each prerequisite relationship is a directed edge.

2. **Cycle Detection**:
   - To determine if all courses can be completed, we need to detect if there is a cycle in the graph. If a cycle exists, then a course depends on itself (directly or indirectly), making it impossible to complete all courses.
   
3. **DFS Traversal**:
   - We perform a depth-first search (DFS) to explore each course and its dependencies. During this process, we track nodes in a "visiting" state (currently being explored). If we encounter a node that is already in the "visiting" state, a cycle is detected.
   
4. **Sets for Tracking**:
   - Use two sets:
     - `visiting`: Nodes currently being explored (to detect cycles).
     - `visited`: Nodes that have been fully explored (to avoid reprocessing).

5. **Return**:
   - If no cycles are detected, return `True` (all courses can be completed). Otherwise, return `False`.

### Function Definition:

```python
def has_cycle(graph, node, visiting, visited):
    """
    Helper function to perform DFS and detect cycles.
    
    :param graph: Adjacency list representing the graph.
    :param node: Current node being visited.
    :param visiting: Set to track nodes currently being visited.
    :param visited: Set to track fully processed nodes.
    :return: False if a cycle is detected, True otherwise.
    """
    pass  # High-level logic explained above.

def course_schedule(num_courses, courses):
    """
    Determines if all courses can be completed given their prerequisites.
    
    :param num_courses: Number of courses.
    :param courses: List of prerequisite pairs.
    :return: True if it's possible to finish all courses, False otherwise.
    """
    pass  # High-level logic explained above.
```

### Function Calls:

1. **Example 1:**
   ```python
   courses = [[1, 0], [0, 1]]
   print(course_schedule(2, courses))  # Expected Output: False (cycle exists)
   ```

2. **Example 2:**
   ```python
   courses = [[1, 0]]
   print(course_schedule(2, courses))  # Expected Output: True (no cycle)
   ```

3. **Example 3:**
   ```python
   courses = [[1, 0], [2, 1], [3, 2]]
   print(course_schedule(4, courses))  # Expected Output: True (no cycle)
   ```

4. **Example 4:**
   ```python
   courses = [[1, 0], [0, 2], [2, 1]]
   print(course_schedule(3, courses))  # Expected Output: False (cycle exists)
   ```
