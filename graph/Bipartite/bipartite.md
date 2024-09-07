### Problem Definition
We are given an **undirected graph** represented as an adjacency list, where each node is represented by an integer and each edge connects two nodes. The task is to determine if the graph is **bipartite**.

A graph is bipartite if we can split its set of nodes into two independent sets such that there are no edges between nodes within the same set. This can be checked by attempting to color the graph using two colors and ensuring that no two adjacent nodes share the same color.

### Function Definition
The function `isBipartite(graph)` will determine whether the given graph is bipartite.

- **Input:**
  - `graph`: A list of lists, where each inner list represents the neighbors of a node.
  
- **Output:**
  - A boolean (`True` or `False`), indicating whether the graph is bipartite.

### Function Logic

1. **Coloring the Graph:**
   - We use a dictionary `color` to keep track of the color assigned to each node (0 or 1).
   - If two connected nodes have the same color, the graph is not bipartite.

2. **Depth-First Search (DFS):**
   - The DFS function (`dfs`) explores the neighbors of a node, assigns the opposite color to its neighbors, and recursively checks for conflicts.
   - If any conflict arises (two adjacent nodes having the same color), the function returns `False`.

3. **Graph Traversal:**
   - Since the graph may be disconnected, we iterate through all nodes, initiating DFS for each unvisited node.

### Function Call Example
The function can be called with various graph inputs:
```python
graph1 = [[1,3], [0,2], [1,3], [0,2]]  # Bipartite graph
graph2 = [[1,2,3], [0,2], [0,1,3], [0,2]]  # Not bipartite
isBipartite(graph2)
```

### High-Level Solution

1. Initialize an empty dictionary `color` to keep track of the color of each node.
2. Define a helper function `dfs(node)` to perform DFS:
   - For each neighbor of the current node, check if it has already been colored:
     - If the neighbor has the same color as the current node, return `False` (not bipartite).
     - Otherwise, assign the opposite color to the neighbor and recursively call `dfs` on it.
3. Iterate through all nodes of the graph. If a node is not colored, initiate DFS from that node and assign an initial color.
4. If any DFS call returns `False`, return `False` (the graph is not bipartite).
5. If all nodes are successfully colored, return `True`.

### Time Complexity:
- **Time Complexity:** O(V + E), where V is the number of vertices (nodes) and E is the number of edges.
  - Each node and edge is visited once in the DFS.
  
- **Space Complexity:** O(V) for the `color` dictionary and recursion stack.

