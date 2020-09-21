def meeting_planner(slotsA, slotsB, dur):
  i = 0
  j = 0
  #Find interval
  while i < len(slotsA) and j < len(slotsB):
    start = max(slotsA[i][0], slotsB[j][0])
    end = min(slotsA[i][1], slotsB[j][1])
    #Check if interval >= dur
    if (start + dur) <= end:
        return [start, start + dur]#return [start_interval, start_interval + 
    
    #increment interval
    if slotsA[i][1] < slotsB[j][1]:
        i+=1
    else:
        j+=1
  
  return []


slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8