
import collections
def majority_element(arr):
    arr.sort()
    return arr[len(arr)//2]

arr = [2,2,1,1,1,2,2]

