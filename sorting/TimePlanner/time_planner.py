def meeting_planner(slotsA, slotsB, dur):
    i = 0
    j = 0

    while i < len(slotsA) and j < len(slotsB):
        max_start = max(slotsA[i][0], slotsB[j][0])
        min_end = min(slotsA[i][1], slotsB[j][1])
        if (min_end - max_start) >= dur:
            return [max_start, max_start + dur]
        
        if slotsA[i][0] < slotsB[j][0]:
            i+=1
        else:
            j+=1

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
result = meeting_planner(slotsA, slotsB, dur)
# Output: [60, 68]
print(result)
