### Problem: Course Schedule II (Leetcode 210)

We are tasked with determining the order in which to take courses given their prerequisites. This problem can be modeled as a **directed graph** where:
- Each course is a node.
- A directed edge from course `A` to course `B` means course `A` is a prerequisite for course `B`.

The goal is to return a valid order in which all courses can be taken. If no such order exists (i.e., there is a cycle), return an empty list.

### High-Level Solution:

This problem is essentially about **Topological Sorting** of a directed graph:
1. **Graph Representation**: Represent courses as nodes and prerequisites as directed edges in a graph.
2. **Cycle Detection**: If there's a cycle, it's impossible to complete all courses.
3. **DFS with Topological Sorting**: Perform Depth-First Search (DFS) to find the topological ordering of nodes (courses). Add a node to the result once all its dependencies (prerequisites) have been processed.

### Function Logic:

1. **Graph Construction**:
   - Build the graph using an adjacency list representation.
   
2. **Cycle Detection and DFS**:
   - Use DFS to detect cycles and also to collect the topological order.
   - Use two sets:
     - `visiting`: Nodes currently being visited (in the DFS call stack).
     - `visited`: Nodes that have been fully processed.
   
3. **Topological Sort**:
   - Perform DFS on each course. If all prerequisites of a course are satisfied, add the course to the result list.
   - If a cycle is detected, return an empty list.
   
4. **Return the Result**:
   - If the graph has no cycles, return the topologically sorted order (reversed list of the result).

### Function Definition:

```python
def has_cycle(ans, graph, node, visiting, visited):
    """
    DFS function to detect cycles and perform topological sort.
    
    :param ans: List to store the topological ordering.
    :param graph: Adjacency list representing the graph.
    :param node: Current node being visited.
    :param visiting: Set of nodes being visited in the current DFS stack.
    :param visited: Set of nodes that have already been processed.
    :return: False if a cycle is detected, True otherwise.
    """
    pass

def course_schedule(num_courses, courses):
    """
    Function to find a valid order of courses or detect if it's impossible.
    
    :param num_courses: Number of courses.
    :param courses: List of prerequisite pairs.
    :return: A valid order of courses if possible, otherwise an empty list.
    """
    pass
```

### Function Calls:

#### Example 1:
```python
courses = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(course_schedule(4, courses))  # Expected Output: [0, 2, 1, 3]
```

**Explanation**: Course `0` has no prerequisites, so it can be taken first. Then either course `2` or `1` can be taken, and finally course `3`, which depends on both `1` and `2`.

#### Example 2:
```python
courses = [[1, 0], [0, 1]]
print(course_schedule(2, courses))  # Expected Output: []
```

**Explanation**: This is a cycle between course `0` and course `1`. Hence, it's impossible to complete the courses, and the function returns an empty list.

#### Example 3:
```python
courses = []
print(course_schedule(1, courses))  # Expected Output: [0]
```

**Explanation**: There is only one course with no prerequisites, so it can be taken without any issue.

### Time Complexity:
- **Time Complexity**: O(V + E), where V is the number of vertices (courses) and E is the number of edges (prerequisite pairs). Each node and edge is visited once during DFS.

### Space Complexity:
- **Space Complexity**: O(V + E), for storing the graph, visiting/visited sets, and the result list.

This solution efficiently handles both cycle detection and topological sorting using depth-first search (DFS).
