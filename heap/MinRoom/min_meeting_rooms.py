import heapq

def minMeetingRooms(intervals):
    """
    Function to determine the minimum number of meeting rooms required.

    Args:
    intervals: List[List[int]] - A list of meeting time intervals.

    Returns:
    int - The minimum number of meeting rooms required.
    """

    # If there are no meetings, we don't need any rooms
    if not intervals:
        return 0

    # Sort the meetings based on start times
    intervals.sort(key=lambda x: x[0])

    # Initialize a heap to keep track of the end times of meetings
    free_rooms = []

    # Add the first meeting's end time to the heap
    heapq.heappush(free_rooms, intervals[0][1])

    # Iterate over the remaining meetings
    for i in intervals[1:]:
        # If the room that frees up the earliest can be reused, pop it from the heap
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        # Push the current meeting's end time onto the heap (whether a new room or reused room)
        heapq.heappush(free_rooms, i[1])

    # The number of rooms required is the size of the heap
    return len(free_rooms)
