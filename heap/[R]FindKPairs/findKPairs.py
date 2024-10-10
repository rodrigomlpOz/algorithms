from typing import List
import heapq

def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    """
    Finds the k pairs with the smallest sums from two sorted arrays.

    Args:
        nums1 (List[int]): First sorted integer array.
        nums2 (List[int]): Second sorted integer array.
        k (int): Number of pairs to return.

    Returns:
        List[List[int]]: List containing k pairs with the smallest sums.
    """
    # Edge Case: If either array is empty or k is 0, return an empty list
    if not nums1 or not nums2 or k == 0:
        return []

    # Initialize the min-heap
    min_heap = []
    # Push the first pair (nums1[0], nums2[0 to min(k, len(nums2))-1])
    for j in range(min(k, len(nums2))):
        # Each heap element is a tuple: (sum, index in nums1, index in nums2)
        heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))
    
    result = []
    
    # Extract the k smallest pairs
    while min_heap and len(result) < k:
        current_sum, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])
        
        # If there is a next element in nums1, push the new pair into the heap
        if i + 1 < len(nums1):
            new_sum = nums1[i + 1] + nums2[j]
            heapq.heappush(min_heap, (new_sum, i + 1, j))
    
    return result

# Example Usage
if __name__ == "__main__":
    # Example 1
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    print(k_smallest_pairs(nums1, nums2, k))  # Output: [[1,2],[1,4],[1,6]]

    # Example 2
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    print(k_smallest_pairs(nums1, nums2, k))  # Output: [[1,1],[1,1]]

    # Example 3
    nums1 = [1,2]
    nums2 = [3]
    k = 3
    print(k_smallest_pairs(nums1, nums2, k))  # Output: [[1,3],[2,3]]

    # Example 4
    nums1 = []
    nums2 = [1,2,3]
    k = 3
    print(k_smallest_pairs(nums1, nums2, k))  # Output: []

    # Example 5
    nums1 = [1,2,3]
    nums2 = [1,2,3]
    k = 5
    print(k_smallest_pairs(nums1, nums2, k))  # Output: [[1,1],[1,2],[2,1],[1,3],[2,2]]
