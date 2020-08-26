import collections
def optimum_assignment(tasks):
    tasks.sort()
    ans = []
    for i in range(len(tasks)//2):
        ans.append((tasks[i], tasks[len(tasks)-1-i]))
    return ans


tasks = [5, 2, 1, 6, 4, 4]
result = optimum_assignment(tasks)
print(result)
