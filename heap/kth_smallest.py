import heapq

def kth_smallest(arr, k):
    heap = []
    for i in range(k):
        heap.append(arr[i])
    heapq.heapify(heap)
    for i in range(k, len(arr)):
        heapq.heappushpop(heap, arr[i])
    return heapq.heappop(heap)



return 13.
'''