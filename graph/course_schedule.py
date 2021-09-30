'''
https://leetcode.com/problems/course-schedule/
'''
import collections
def has_cycle(graph,node, visiting, visited):
    if node in visiting:
        return False
    visiting.add(node)
    for nei in graph[node]:
        if nei not in visited and not has_cycle(graph,nei, visiting, visited):
            return False
    visiting.remove(node)
    visited.add(node)
    return True

def course_schedule(num_courses,courses):
    visiting = set()
    visited = set()
    course_codes = []
    for i in range(num_courses):
        course_codes.append(i)

    graph = collections.defaultdict(list)
    for course_pair in courses:
        prereq, course = course_pair[1], course_pair[0]
        graph[prereq].append(course)
    for course in course_codes:
        if course not in visited and not has_cycle(graph, course, visiting, visited):
            return False
    return True

courses = [[1,0],[0,1]]
print(course_schedule(2, courses))


print("hello")
