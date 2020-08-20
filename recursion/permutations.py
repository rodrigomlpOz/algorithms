def permutation(arr):
    ans = []
    temp = []
    def recurse(arr, ans, temp):
        if len(temp) == len(arr):
            ans.append(temp[:])
        for num in arr:
            if num in temp:
                continue
                
            temp.append(num)
            
            recurse(arr, ans, temp)

            temp.pop()
    recurse(arr, ans, temp)
    return ans
        

arr = [1,2,3]
ans = permutation(arr)
print(ans)