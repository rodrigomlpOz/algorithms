def mergeIntervals(A, B):
    result = []  # This will store the merged intervals
    i, j = 0, 0  # Two pointers for traversing lists A and B

    # Helper function to merge two overlapping intervals
    def merge(current, new_interval):
        return [min(current[0], new_interval[0]), max(current[1], new_interval[1])]

    # Traverse both lists A and B using two pointers
    while i < len(A) and j < len(B):
        # Pick the interval with the smaller start time
        if A[i][0] < B[j][0]:
            interval = A[i]
            i += 1
        else:
            interval = B[j]
            j += 1

        # If result is empty or there is no overlap with the last interval in result, add the interval
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            # There is an overlap, merge the intervals
            result[-1] = merge(result[-1], interval)

    # If there are remaining intervals in A, add or merge them into the result
    while i < len(A):
        if result[-1][1] < A[i][0]:
            result.append(A[i])  # No overlap, add directly
        else:
            result[-1] = merge(result[-1], A[i])  # Merge overlapping intervals
        i += 1

    # If there are remaining intervals in B, add or merge them into the result
    while j < len(B):
        if result[-1][1] < B[j][0]:
            result.append(B[j])  # No overlap, add directly
        else:
            result[-1] = merge(result[-1], B[j])  # Merge overlapping intervals
        j += 1

    return result  # Return the final merged list of intervals
