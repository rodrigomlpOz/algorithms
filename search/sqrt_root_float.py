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
    mid = (h+l)/2
    while abs((mid*mid) - num) > 0.001:
        mid = (h+l)/2
        if (mid * mid) > num:
            h = mid + 1
        else:
            l = mid - 1
    return mid

num = 6
ans = val_equal_index(num)
print(ans)