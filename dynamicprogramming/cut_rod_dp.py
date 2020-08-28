'''
C(i) = max{V[k] + C(i-k)}
       1 < k < i
'''
# Returns the best obtainable price for a rod of length n  
# and price[] as prices of different pieces 
def cutRod(price, n): 
    if(n <= 0): 
        return 0
    max_val = float('-inf')
      
    # Recursively cut the rod in different pieces   
    # and compare different configurations 
    for i in range(0, n): 
        max_val = max(max_val, price[i] + 
                      cutRod(price, n - i - 1)) 
    return max_val 
  
# Driver code 
arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr) 
r = cutRod(arr, size)
print(r)


    
