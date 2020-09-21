
import collections
def three_sum(arr, s):
    n = len(arr)
    if n < 3:
        return []
    arr.sort()
    for i in range(len(arr)-2):
            r = s - arr[i]
            l = i+1
            h = n - 1
            while l < h:
                if (arr[l] + arr[h] < r):
                    l += 1
                elif (arr[l] + arr[h] > r):
                    h -= 1
                else:
                    return [arr[i], arr[l], arr[h]]
    return []
arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 16
result = three_sum(arr, s)
print(result)

