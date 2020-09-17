def bracket_match(text):
  
  diff, mis = 0, 0
  
  for c in text:
    if c == '(': diff += 1
    if c == ')': diff -= 1
    if diff < 0: 
      mis += 1
      diff = 0
      
  return mis + diff