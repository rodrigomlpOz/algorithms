import heapq

def kthSmallest(matrix, k):
    """
    Finds the k-th smallest element in an n x n sorted matrix.

    Args:
    matrix (List[List[int]]): The n x n matrix with sorted rows and columns.
    k (int): The order of the smallest element to find.

    Returns:
    int: The k-th smallest element in the matrix.
    """
    if not matrix or not matrix[0]:
        raise ValueError("Matrix is empty or not properly formatted.")

    n = len(matrix)
    min_heap = []
    visited = set()

    # Initialize the heap with the first element
    heapq.heappush(min_heap, (matrix[0][0], 0, 0))
    visited.add((0, 0))

    while min_heap:
        current, row, col = heapq.heappop(min_heap)
        k -= 1

        if k == 0:
            return current

        # Move Right
        if col + 1 < len(matrix[0]) and (row, col + 1) not in visited:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
            visited.add((row, col + 1))
            # Example Scenario:
            # Suppose we're at position (0, 1). Without the visited set,
            # the element at (1, 1) could be added again when moving down from (0, 1).

        # Move Down
        if row + 1 < n and (row + 1, col) not in visited:
            heapq.heappush(min_heap, (matrix[row + 1][col], row + 1, col))
            visited.add((row + 1, col))
            # Example Scenario:
            # Suppose we're at position (1, 0). Without the visited set,
            # the element at (1, 1) could be added again when moving right from (1, 0).

    raise ValueError("k is larger than the number of elements in the matrix.")
