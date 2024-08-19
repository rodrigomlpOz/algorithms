def val_equal_index(num):
    l = 0
    h = num
    while l <= h:
        mid = (l + h) // 2
        if mid * mid <= num < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > num:
            h = mid - 1
        else:
            l = mid + 1
    return l

num = 300
ans = val_equal_index(num)
print(ans)  # Expected output: 17
