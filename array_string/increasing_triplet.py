def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c1, c2 = float('inf'), float('inf')
        for x in nums:
            if (x <= c1): 
                c1 = x         
            elif (x <= c2):  
                c2 = x           
            else:             
                return True 
        return False