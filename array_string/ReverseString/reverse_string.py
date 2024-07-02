'''
https://leetcode.com/problems/reverse-words-in-a-string/solution/

https://www.pramp.com/challenge/VKdqbrq6B1S5XAyGAOn4
'''

def trim_spaces(s):
    left, right = 0, len(s) - 1
    # remove leading spaces
    while left <= right and s[left] == ' ':
        left += 1
    
    # remove trailing spaces
    while left <= right and s[right] == ' ':
        right -= 1
    
    # reduce multiple spaces to single one
    output = []
    while left <= right:
        if s[left] != ' ':
            output.append(s[left])
        elif output[-1] != ' ':
            output.append(s[left])
        left += 1
    
    return output
        
def reverse(l, left, right):
    while left < right:
        l[left], l[right] = l[right], l[left]
        left, right = left + 1, right - 1
        
def reverse_each_word(l):
    n = len(l)
    start = end = 0
    
    while start < n:
        # go to the end of the word
        while end < n and l[end] != ' ':
            end += 1
        # reverse the word
        reverse(l, start, end - 1)
        # move to the next word
        start = end + 1
        end += 1
            
def reverseWords(s):
    # converst string to char array 
    # and trim spaces at the same time
    l = trim_spaces(s)
    
    # reverse the whole string
    reverse(l, 0, len(l) - 1)
    
    # reverse each word
    reverse_each_word(l)
    
    return ''.join(l)

arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
