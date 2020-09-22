'''
Grea explanation of this approach
'''
class Solution:
    def change(self, amount, coins):

        # base case:
        # amount 0's method count = 1 (by taking no coins)
        change_method_count = [1] + [ 0 for _ in range(amount)]
        
        # make change with current coin, from small coin to large coin
        for cur_coin in coins:
            
            # update change method count from small amount to large amount
            for small_amount in range(cur_coin, amount+1):
                
                # current small amount can make changed with current coin
                change_method_count[small_amount] += change_method_count[small_amount - cur_coin]
                
        return change_method_count[amount]