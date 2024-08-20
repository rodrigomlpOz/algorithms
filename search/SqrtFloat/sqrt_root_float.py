def val_equal_index(num):
    l = 0
    h = num
    mid = (h + l) / 2
    
    while abs((mid * mid) - num) > 0.001:  # Adjust precision as needed
        if mid * mid > num:
            h = mid  # Move the high pointer down
        else:
            l = mid  # Move the low pointer up
        mid = (h + l) / 2  # Recalculate mid

    return mid

num = 6
ans = val_equal_index(num)
print(ans)  # Expected output: Approximately 2.449
