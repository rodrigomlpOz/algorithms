import heapq
def sort_approximately_sorted_array(sequence,k):

    min_heap = []
    # Adds the first k elements into min_heap. Stop if there are fewer than k
    # elements.
    for i in range(k):
        heapq.heappush(min_heap, sequence[i])

    result = []
    # For every new element, add it to min_heap and extract the smallest.
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # sequence is exhausted, iteratively extracts the remaining elements.
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result
