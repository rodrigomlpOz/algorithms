import heapq

def merge_sorted_arrays(sorted_subarrays):
    """
    Merges multiple sorted arrays into one sorted array.
    
    Args:
    sorted_subarrays: List[List[int]] - A list of sorted subarrays.
    
    Returns:
    List[int] - A single merged and sorted array.
    """
    min_heap = []
    result = []
    
    # Initialize the heap with the first element of each sorted subarray.
    sorted_iters = [iter(x) for x in sorted_subarrays]
    
    for i, it in enumerate(sorted_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
    
    while min_heap:
        smallest, idx = heapq.heappop(min_heap)
        result.append(smallest)
        next_element = next(sorted_iters[idx], None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, idx))
    
    return result

def sort_k_increasing_decreasing_array(A):
    """
    Sorts an array consisting of k increasing and decreasing subarrays.
    
    Args:
    A: List[int] - The input array.
    
    Returns:
    List[int] - A fully sorted array.
    """
    sorted_subarrays = []
    increasing, decreasing = range(2)
    subarray_type = increasing
    start_idx = 0

    # Decompose the array into k sorted subarrays.
    for i in range(1, len(A) + 1):
        if (i == len(A) or  # A is ended. Adds the last subarray.
            (A[i - 1] < A[i] and subarray_type == decreasing) or
            (A[i - 1] >= A[i] and subarray_type == increasing)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type ==
                                    increasing else A[i - 1:start_idx - 1:-1])
            start_idx = i
            subarray_type = (decreasing if subarray_type == increasing else increasing)

    # Merge all sorted subarrays into one sorted array.
    return merge_sorted_arrays(sorted_subarrays)
