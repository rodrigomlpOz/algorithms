def val_equal_index(arr):
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = (h+l)//2
        if mid == arr[mid]:
            return mid
        elif arr[mid] < mid:
            l = mid
        else:
            h = mid
    return

arr = [-2, 0, 2, 5, 6, 7, 9]
val_equal_index(arr)
