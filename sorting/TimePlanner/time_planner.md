### Problem Definition:
Given two people’s availability slots (represented as time intervals) and a meeting duration, find the earliest time slot that works for both people where the meeting can be scheduled.

### Functional Definition:
1. **Function Name:** `meeting_planner`
2. **Input Parameters:**
   - `slotsA` (List of lists): Available time slots for person A. Each slot is a list `[start, end]` where `start` and `end` are integers representing time in minutes.
   - `slotsB` (List of lists): Available time slots for person B. Each slot is a list `[start, end]`.
   - `dur` (Integer): The required meeting duration in minutes.

3. **Output:**
   - A list `[start, end]` representing the start and end time of the earliest available slot that can accommodate the meeting. If no such slot exists, return an empty list `[]`.

4. **Example Call:**
   ```python
   slotsA = [[10, 50], [60, 120], [140, 210]]
   slotsB = [[0, 15], [60, 70]]
   dur = 8
   result = meeting_planner(slotsA, slotsB, dur)
   # Output: [60, 68]
   ```

### High-Level Solution:
1. **Pointers Approach:**
   - Use two pointers `i` and `j` to traverse the available slots for person A and person B respectively.
   - For each slot pair, find the overlapping time using the `max(start times)` and `min(end times)` of the two slots.
   - If the overlap is greater than or equal to the meeting duration (`dur`), return the earliest start time for the meeting.
   - Move the pointer for the slot that ends earlier to consider the next available interval.
   - If no such slot is found, return an empty list.
