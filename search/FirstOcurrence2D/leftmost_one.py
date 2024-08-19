def binarySearch(A):
    lo, hi = 0, len(A)
    target = 1
    while lo < hi:
        mid = (lo + hi) // 2
        if A[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

def leftmost_one(matrix):
    min_idx = float('inf')
    for row in matrix:
        min_idx = min(min_idx, binarySearch(row))
    return min_idx
