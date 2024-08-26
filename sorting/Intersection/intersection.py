def intersection(arr1, arr2):
    i = 0
    j = 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:  
            if i == 0 or arr1[i-1] != arr1[i]:
                ans.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:          
            i += 1
        else:
            j += 1
    return ans
    


arr1 = [2,3,3,5,5,6,7,7,8,12]
arr2 = [5,5,6,8,8,9,10,10]
ans = intersection(arr1, arr2)
print(ans)
