def first_ocurrunce(arr, k):
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = (h+l)//2
        if arr[mid] == k and (mid == 0 and arr[mid-1] != arr[mid]):
            return mid
        elif arr[mid] < k:
            l = mid + 1
        else:
            h = mid
    return -1

arr = [0, 1]
ans = first_ocurrunce(arr, 1)
print(arr)