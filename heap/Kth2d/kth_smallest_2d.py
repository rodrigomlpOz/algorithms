import heapq

def kth_two(matrix, k):
    result, heap = None, []
    n = len(matrix)

    # Push the first element from the matrix into the heap along with its position
    heapq.heappush(heap, (matrix[0][0], 0, 0))
    
    while k > 0:
        # Pop the smallest element from the heap
        result, i, j = heapq.heappop(heap)

        # Push the next element in the same row if it exists
        if i == 0 and j + 1 < n:
            heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))

        # Push the next element in the same column if it exists
        if i + 1 < n:
            heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
        
        # Decrease k as we are processing one element at a time
        k -= 1

    return result
