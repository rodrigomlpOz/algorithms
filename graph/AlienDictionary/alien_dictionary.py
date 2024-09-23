from collections import defaultdict

def alienOrder(words):
    graph = defaultdict(list)
    visiting = set()  # Nodes currently in the DFS path
    visited = set()   # Nodes that have been fully processed
    result = []       # Stack to store the topological order (in reverse)

    # Build graph by comparing adjacent words
    def buildEdge(word1, word2):
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            if word1[i] != word2[i]:
                graph[word1[i]].append(word2[i])
                break
        # If word2 is a prefix of word1, the order is invalid
        if len(word2) < len(word1) and word1.startswith(word2):
            return False
        return True
    
    # Build the graph edges
    for i in range(1, len(words)):
        if not buildEdge(words[i-1], words[i]):
            return ""
    
    # DFS to visit nodes
    def dfs(node):
        if node in visiting:  # Cycle detected
            return False
        if node in visited:  # Already processed, no need to visit again
            return True
        
        # Mark the node as bxeing visited
        visiting.add(node)
        
        # Visit all the neighbors (recursive DFS)
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        
        # Mark the node as fully processed
        visiting.remove(node)
        visited.add(node)
        
        # Add the node to the result (stack) in reverse order
        result.append(node)
        return True
    
    # Initialize graph with all unique characters
    unique_chars = set(''.join(words))
    
    # Perform DFS on each unvisited node
    for char in unique_chars:
        if char not in visited:
            if not dfs(char):
                return ""  # Cycle detected, return empty string
    
    # The result list will contain the reverse topological order, so reverse it
    return ''.join(result[::-1])

# Test the function
words = ["wrt", "wrf", "er", "ett", "rftt"]
result = alienOrder(words)
print(result)  # Expected output: "wertf"
