import heapq

def maxSlidingWindowHeap(nums, k):
    """
    Finds the maximum value in each sliding window of size k using a max-heap.
    
    Args:
    nums (List[int]): The list of integers.
    k (int): The size of the sliding window.
    
    Returns:
    List[int]: A list containing the maximum values for each sliding window.
    """
    if not nums or k == 0:
        return []

    result = []
    max_heap = []  # Heap to store elements as (-value, index) for max-heap behavior

    for i in range(len(nums)):
        # Push current element with negative value to simulate max-heap
        heapq.heappush(max_heap, (-nums[i], i))

        # Remove elements not in the current window
        while max_heap[0][1] < i - k + 1:
            heapq.heappop(max_heap)

        # Record the current maximum
        if i >= k - 1:
            result.append(-max_heap[0][0])

    return result

# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindowHeap(nums, k))  # Expected output: [3, 3, 5, 5, 6, 7]
