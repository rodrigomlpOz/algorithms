def coin_change_ways(amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        #If we found a way to create the desired amount
        if amount == 0: 
            return 1 
        
        #If we went over our amount or we have no more coins left
        if amount < 0 or len(coins) == 0:
            return 0 

        #Our solutions can be divided into two sets,
        #   1) Solutions that cointain the coin at the end of the coins array 
        #   2) Solutions that don't contain that coin 
        return coin_change_ways(amount - coins[-1], coins) + coin_change_ways(amount, coins[:-1])