def val_equal_index(arr):
    l = 0
    h = len(arr)-1
    while l < h:
        mid = (h+l)//2
        if arr[mid] > arr[h]:
            l = mid + 1
        else:
            h = mid
    return l

arr = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
val_equal_index(arr)
