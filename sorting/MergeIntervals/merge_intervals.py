def merge(intervals):
    # If the list is empty, return an empty list
    if not intervals:
        return []
    
    # Sort the intervals by the start time
    intervals.sort(key=lambda x: x[0])
    
    # Initialize the merged intervals list with the first interval
    merged = [intervals[0]]
    
    # Iterate through the sorted intervals
    for i in range(1, len(intervals)):
        # Get the last interval in the merged list
        last_merged = merged[-1]
        
        # If the current interval overlaps with the last merged interval
        if intervals[i][0] <= last_merged[1]:
            # Merge them by updating the end of the last merged interval
            merged[-1][1] = max(last_merged[1], intervals[i][1])
        else:
            # If they don't overlap, simply add the current interval
            merged.append(intervals[i])
    
    return merged
