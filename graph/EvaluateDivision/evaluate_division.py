from collections import defaultdict
from typing import List

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    # Build the graph
    graph = defaultdict(dict)
    for (A, B), value in zip(equations, values):
        graph[A][B] = value
        graph[B][A] = 1 / value

    # DFS helper function
    def dfs(start: str, end: str, visited: set) -> float:
        if start == end:
            return 1.0
        visited.add(start)

        for neighbor, value in graph[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return value * result

        return -1.0

    # Evaluate each query
    results = []
    for C, D in queries:
        if C not in graph or D not in graph:
            results.append(-1.0)
        else:
            results.append(dfs(C, D, set()))

    return results

# Example test case
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

# Running the function with the test case
print(calcEquation(equations, values, queries))
