import collections

def has_cycle(ans, graph, node, visiting, visited):
    if node in visiting:
        return True  # Cycle detected
    if node in visited:
        return False  # No cycle, already processed
    
    # Mark the node as being visited
    visiting.add(node)
    
    # Visit all the neighbors (prerequisites)
    for nei in graph[node]:
        if has_cycle(ans, graph, nei, visiting, visited):
            return True  # Cycle detected
    
    # Mark the node as fully processed
    visiting.remove(node)
    visited.add(node)
    
    # Append the node to the result (reverse topological order)
    ans.append(node)
    return False  # No cycle

def course_schedule(num_courses, courses):
    visiting = set()
    visited = set()
    ans = []
    
    # Build the graph
    graph = collections.defaultdict(list)
    for course_pair in courses:
        prereq, course = course_pair[1], course_pair[0]
        graph[prereq].append(course)
    
    # Perform DFS on each course
    for course in range(num_courses):
        if course not in visited:
            if has_cycle(ans, graph, course, visiting, visited):
                return []  # Cycle detected, no valid order
    
    # Reverse the result to get the correct topological order
    return ans[::-1]

# Test the function
courses = [[1,0],[2,0],[3,1],[3,2]]
print(course_schedule(4, courses))  # Expected output: [0, 1, 2, 3] or [0, 2, 1, 3]
