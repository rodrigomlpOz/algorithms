'''
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
def first_ocurrunce(arr, k):
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = (h+l)//2
        if mid == 0 or (arr[mid] == k and arr[mid-1] != arr[mid]):
            return mid
        elif arr[mid] < k:
            l = mid
        else:
            h = mid
    return

arr = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
arr1 = [285]
k = 1
first_ocurrunce(arr1, k)