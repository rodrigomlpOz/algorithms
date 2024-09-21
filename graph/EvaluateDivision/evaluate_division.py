from collections import defaultdict
from typing import List

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """
    Calculates the result of division for each query based on the given equations and values.

    Args:
    - equations: List of equations represented as pairs of variables.
    - values: List of real numbers representing the division results of the equations.
    - queries: List of queries represented as pairs of variables.

    Returns:
    - List of results for each query. If a query cannot be determined, returns -1.0.
    """
    # Step 1: Build the graph
    graph = defaultdict(list)  # Adjacency list representation

    # Populate the graph with the given equations and values
    for (A, B), value in zip(equations, values):
        graph[A].append((B, value))        # A / B = value
        graph[B].append((A, 1 / value))    # B / A = 1/value

    def dfs(start: str, end: str, visited: set) -> float:
        """
        Performs Depth-First Search (DFS) to find the product of edge weights from start to end.

        Args:
        - start: The starting variable.
        - end: The target variable.
        - visited: A set to keep track of visited variables to avoid cycles.

        Returns:
        - The division result if a path exists, otherwise -1.0.
        """
        if start == end:
            return 1.0  # Any variable divided by itself is 1.0

        visited.add(start)  # Mark the current variable as visited

        for neighbor, value in graph[start]:
            if neighbor in visited:
                continue  # Skip already visited variables to prevent cycles
            result = dfs(neighbor, end, visited)
            if result != -1.0:
                return value * result  # Multiply the edge weight with the result from the neighbor

        return -1.0  # No path found from start to end

    results = []  # To store the results of each query

    # Step 2: Process each query
    for C, D in queries:
        if C not in graph or D not in graph:
            # If either variable is undefined, append -1.0
            results.append(-1.0)
        elif C == D:
            # If both variables are the same and defined, append 1.0
            results.append(1.0)
        else:
            visited = set()  # Initialize an empty set for visited variables
            result = dfs(C, D, visited)  # Perform DFS to find the result
            results.append(result)  # Append the result to the results list

    return results  # Return all query results
