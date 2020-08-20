def power_set(arr):
    ans = []
    temp = []
    def recurse(arr, ans, temp, pos):
        ans.append(temp[:])
        for i in range(pos, len(arr)):
            temp.append(arr[i])

            recurse(arr, ans, temp, i+1)

            temp.pop()
    recurse(arr, ans, temp, 0)
    return ans
        

arr = [1, 2, 3]
ans = power_set(arr)
print(ans)