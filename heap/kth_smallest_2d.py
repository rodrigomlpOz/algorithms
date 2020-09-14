import heapq
def kth_two(matrix, k):
    result, heap = None, []
    heapq.heappush(heap, (matrix[0][0], 0, 0))
    while k > 0:
        result, i, j = heapq.heappop(heap)
        if i == 0 and j + 1 < len(matrix):
            heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        if i + 1 < len(matrix):
            heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
        k -= 1
    return result



matrix = [[ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
ans = kth_two(matrix, k)
print(ans)
'''
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
'''