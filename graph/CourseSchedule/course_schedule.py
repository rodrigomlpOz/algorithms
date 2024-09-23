import collections

def has_cycle(graph, node, visiting, visited):
    if node in visiting:
        return True  # Cycle detected
    if node in visited:
        return False  # No cycle, already processed
    
    # Mark the node as being visited
    visiting.add(node)
    
    # Visit all the neighbors (prerequisites)
    for nei in graph[node]:
        if has_cycle(graph, nei, visiting, visited):
            return True  # Cycle detected
    
    # Mark the node as fully processed
    visiting.remove(node)
    visited.add(node)
    return False  # No cycle found

def course_schedule(num_courses, prerequisites):
    visiting = set()
    visited = set()
    
    # Build the graph
    graph = collections.defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # Perform DFS on each course
    for course in range(num_courses):
        if course not in visited:
            if has_cycle(graph, course, visiting, visited):
                return False  # Cycle detected, cannot finish all courses
    
    return True  # No cycle, can finish all courses

# Test the function
courses = [[1,0],[0,1]]  # This has a cycle
print(course_schedule(2, courses))  # Expected output: False

courses = [[1,0]]  # No cycle, 0 -> 1
print(course_schedule(2, courses))  # Expected output: True
