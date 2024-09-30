### Problem Statement:
You are given a list of events, where each event is defined by a start time and a finish time. Your task is to determine the maximum number of events that occur simultaneously at any given time.

### Functional Definition:

**Function Name**: `find_max_simultaneous_events`

**Input Parameters**:
- `events` (List of tuples): A list of events, where each event is represented by a tuple `(start, finish)`:
  - `start` (int): The start time of the event.
  - `finish` (int): The finish time of the event.

**Output**:
- An integer representing the maximum number of events that overlap (i.e., the maximum number of events occurring simultaneously at the same time).

### Example Call:

```python
events = [
    (1, 5),
    (2, 7),
    (4, 5),
    (6, 10),
    (8, 9)
]

result = find_max_simultaneous_events(events)
print(result)  # Output: 3
```

### High-Level Solution:

1. **Event Representation**:
   - Each event is represented as a tuple `(start, finish)` where `start` is the time the event begins and `finish` is the time the event ends.
   
2. **Endpoints Construction**:
   - For each event, we create two points (or "endpoints"): one for the start time and one for the finish time. These will help us track when events begin and end.

3. **Sorting the Endpoints**:
   - We create a list of endpoints consisting of the start and finish times of all events. Each endpoint is a tuple `(time, is_start)` where:
     - `time` is the event time (either start or finish).
     - `is_start` is a boolean indicating whether the event is starting (`True`) or ending (`False`).
   - We sort these endpoints by time, giving priority to start times when two events share the same time (so we correctly count overlapping events).

4. **Counting Simultaneous Events**:
   - We traverse the sorted list of endpoints, maintaining a counter for the number of events that are active at each point in time.
   - We increment the counter when an event starts and decrement it when an event ends.
   - Track the maximum number of simultaneous events encountered during this traversal.

5. **Return Result**:
   - The maximum value of simultaneous events encountered during the traversal is the solution, representing the maximum number of overlapping events.

### Code Implementation:

```python
def find_max_simultaneous_events(events):
   pass
```

### Example Walkthrough:
For the input:
```python
events = [
    (1, 5),
    (2, 7),
    (4, 5),
    (6, 10),
    (8, 9)
]
```

- Events start and end at: `{(1, 5), (2, 7), (4, 5), (6, 10), (8, 9)}`
- At time 4, three events overlap: `{(1, 5), (2, 7), (4, 5)}`.

Thus, the function returns `3` as the maximum number of overlapping events.
