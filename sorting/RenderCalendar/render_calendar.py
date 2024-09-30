def find_max_simultaneous_events(events):
    # Step 1: Create a list of all event endpoints (start and finish times)
    endpoints = []
    
    for start, finish in events:
        # (time, is_start) -> is_start = True for starting event, False for ending event
        endpoints.append((start, True))  # True indicates a start time
        endpoints.append((finish, False))  # False indicates an end time

    # Step 2: Sort the list of endpoints
    # First by time, then prioritize start events over end events if times are the same
    #Since True > False in Python, if we sort directly by x[1], the end events (False) will come before start events (True), 
    #which is the opposite of what we want. We want start events to come first, so using not x[1] flips the priority to sort start events (True) before end events (False).
    endpoints.sort(key=lambda x: (x[0], not x[1]))

    # Step 3: Traverse the sorted endpoints to find the maximum number of overlapping events
    max_simultaneous = 0
    current_simultaneous = 0
    
    for time, is_start in endpoints:
        if is_start:
            current_simultaneous += 1
            max_simultaneous = max(max_simultaneous, current_simultaneous)
        else:
            current_simultaneous -= 1
    
    return max_simultaneous
