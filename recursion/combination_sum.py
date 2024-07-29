def combination_sum(arr, target):
    ans = []
    temp = []
    def recurse(arr, ans, temp, target, pos):
        if target < 0:
            return
        elif target == 0:
            ans.append(temp[:])
            return  
        else:
            for i in range(pos,len(arr)):
                temp.append(arr[i])
            
                recurse(arr, ans, temp, target - arr[i], i)

                temp.pop()
    recurse(arr, ans, temp, target, 0)
    return ans
        

candidates = [2,3,5]
target = 8
combination_sum(candidates, target)
