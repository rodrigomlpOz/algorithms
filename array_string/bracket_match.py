'''
A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, 
and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing 
brackets at the end, so you’d return 2.
Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns 
the minimum number of brackets you’d need to add to the input in order to make it correctly matched.
'''
def bracket_match(text):
  
  diff, mis = 0, 0
  
  for c in text:
    if c == '(': diff += 1
    if c == ')': diff -= 1
    if diff < 0: 
      mis += 1
      diff = 0
      
  return mis + diff
