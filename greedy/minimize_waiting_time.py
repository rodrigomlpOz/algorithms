
import collections
def minimize_waiting(arr):
    arr.sort()
    ans = 0
    for i, val in enumerate(arr):
        service_time = len(arr) - (i + 1)
        ans += (service_time * val)
    return ans

arr = [2, 5, 1, 3]
result = minimize_waiting(arr)
print(result)
