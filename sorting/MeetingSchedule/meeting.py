def canAttendMeetings(intervals):
    # If there are no meetings, the person can attend all (i.e., no conflicts)
    if not intervals:
        return True
    
    # Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])
    
    # Iterate through the sorted meetings and check for conflicts
    for i in range(1, len(intervals)):
        # If the current meeting starts before the previous meeting ends, there's a conflict
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    
    # If no conflicts are found, return True
    return True