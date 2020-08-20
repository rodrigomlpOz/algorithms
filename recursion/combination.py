def power_set(n, k):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    ans = []
    temp = []
    def recurse(arr, ans, temp, pos):
        if len(temp) == k:
            ans.append(temp[:])
        for i in range(pos, len(arr)):
            temp.append(arr[i])

            recurse(arr, ans, temp, i+1)

            temp.pop()
    recurse(arr, ans, temp, 0)
    return ans
        

n = 4
k = 2
ans = power_set(n, k)
print(ans)