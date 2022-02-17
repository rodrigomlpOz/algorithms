'''
Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if the length of the rod is 8 and the values of different pieces are given as the following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

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


    
