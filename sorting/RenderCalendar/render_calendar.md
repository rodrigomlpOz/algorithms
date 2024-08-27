### Problem Statement:
You are given a list of events, where each event is defined by a start time and a finish time. Your task is to determine the maximum number of events that are occurring simultaneously.

### Functional Definition:
1. **Function Name:** `find_max_simultaneous_events`
2. **Input Parameters:**
   - `events` (List of `Event` namedtuples): A list of events, where each event is represented by a named tuple `Event(start, finish)`.
   - Each event has:
     - `start`: The start time of the event (an integer).
     - `finish`: The finish time of the event (an integer).

3. **Output:**
   - An integer representing the maximum number of events that overlap (i.e., the maximum number of events that are occurring at the same time).

4. **Example Call:**
   ```python
   events = [
       Event(1, 5),
       Event(2, 7),
       Event(4, 5),
       Event(6, 10),
       Event(8, 9)
   ]
   result = find_max_simultaneous_events(events)
   # Output: 3
   ```

### High-Level Solution:
1. **Event Representation:**
   - Use a named tuple `Event` to represent each event with `start` and `finish` times.
   - Additionally, represent each event's start and finish as "endpoints" using another named tuple `Endpoint`.

2. **Endpoints Construction:**
   - For each event, create two endpoints: one for the start time (`is_start=True`) and one for the finish time (`is_start=False`).
   - Store all endpoints in a list.

3. **Sorting the Endpoints:**
   - Sort the list of endpoints primarily by time. If two events have the same time, prioritize the start event over the finish event (to ensure overlapping events are counted correctly).

4. **Simultaneous Events Calculation:**
   - Traverse the sorted list of endpoints, maintaining a counter for the number of simultaneous events.
   - Increment the counter when an event starts and decrement it when an event ends.
   - Track the maximum number of simultaneous events encountered during the traversal.

5. **Return Result:**
   - The maximum value of simultaneous events encountered during the traversal is the solution.

### Explanation:
- **Event Construction:** Each event is represented by its start and finish times. By constructing a list of these endpoints, we can effectively track when events are overlapping.
- **Sorting and Traversal:** Sorting ensures that we process events in chronological order, and by handling start events before end events at the same time, we accurately count overlapping events.
- **Final Output:** The function returns the maximum number of events that overlap at any given time, which is the desired result.
