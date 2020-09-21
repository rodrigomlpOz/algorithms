
import collections
def four_sum(arr, s):
    n = len(arr)
    if n < 3:
        return []
    arr.sort()
    for i in range(len(arr)-3):
        for j in range(i+1, len(arr)-2):
            r = s - (arr[i] + arr[j])
            l = j+1
            h = n - 1
            while l < h:
                if (arr[l] + arr[h] < r):
                    l += 1
                elif (arr[l] + arr[h] > r):
                    h -= 1
                else:
                    return [arr[i], arr[j], arr[l], arr[h]]
    return []
arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 23
result = four_sum(arr, s)
print(result)
