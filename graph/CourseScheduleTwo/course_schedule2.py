'''
https://leetcode.com/problems/course-schedule-ii/
'''
import collections
def has_cycle(ans, graph, node, visiting, visited):
    if node in visiting:
        return False
    visiting.add(node)
    for nei in graph[node]:
        if nei not in visited and not has_cycle(ans, graph, nei, visiting, visited):
            return False
    visiting.remove(node)
    ans.append(node)
    visited.add(node)
    return True

def course_schedule(num_courses,courses):
    visiting = set()
    visited = set()
    course_codes = []
    for i in range(num_courses):
        course_codes.append(i)
    ans = []
    graph = collections.defaultdict(list)
    for course_pair in courses:
        prereq, course = course_pair[1], course_pair[0]
        graph[prereq].append(course)
    for course in course_codes:
        if course not in visited and not has_cycle(ans, graph, course, visiting, visited):
            return []
    return ans[::-1]

courses = [[1,0],[2,0],[3,1],[3,2]]
print(course_schedule(4, courses))
