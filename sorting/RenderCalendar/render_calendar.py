from collections import namedtuple
from typing import List

# Define the Event as a named tuple with 'start' and 'finish' attributes
Event = namedtuple('Event', ('start', 'finish'))

def find_max_simultaneous_events(events: List[Event]) -> int:
    # Define Endpoint as a named tuple with 'time' and 'is_start' attributes
    Endpoint = namedtuple('Endpoint', ('time', 'is_start'))

    # Create a list of all start and end points
    endpoints = []
    for event in events:
        endpoints.append(Endpoint(event.start, True))   # True indicates the start of an event
        endpoints.append(Endpoint(event.finish, False)) # False indicates the end of an event

    # Sort the endpoints by time. If two times are the same, prioritize start events
    endpoints.sort(key=lambda e: (e.time, not e.is_start))

    max_simultaneous_events = 0
    current_simultaneous_events = 0

    # Traverse the sorted endpoints to determine the maximum number of simultaneous events
    for endpoint in endpoints:
        if endpoint.is_start:
            # Increment the count when an event starts
            current_simultaneous_events += 1
            # Update the maximum count if needed
            max_simultaneous_events = max(max_simultaneous_events, current_simultaneous_events)
        else:
            # Decrement the count when an event ends
            current_simultaneous_events -= 1

    return max_simultaneous_events

# Example usage
events = [
    Event(1, 5),
    Event(2, 7),
    Event(4, 5),
    Event(6, 10),
    Event(8, 9)
]
print(find_max_simultaneous_events(events))  # Output: 3
