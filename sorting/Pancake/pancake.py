def flip(arr, k):
    start = 0
    end = k
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def find_max_idx(arr, idx):
    max_val = float('-inf')
    max_idx = -1

    for i in range(idx+1):
        if arr[i] > max_val:
            max_val = arr[i] 
            max_idx = i 
    return max_idx

def pancake_sort(arr):
    for i in reversed(range(len(arr))):
        idx = find_max_idx(arr, i)
        flip(arr, idx)
        flip(arr, i)
    print(arr)

arr = [5, 2, 3, 1,4]
