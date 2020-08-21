'''
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
def val_equal_index(num):
    l = 0
    h = num-1
    mid = (h+l)//2
    while l <= h:
        mid = (h+l)//2
        if (mid)*(mid) <= num < (mid+1)*(mid+1):
            return mid
        elif (mid * mid) > num:
            h = mid + 1
        else:
            l = mid - 1
    return l

num = 300
ans = val_equal_index(num)
print(ans)