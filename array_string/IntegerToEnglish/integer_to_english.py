def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # Define arrays for number-to-word mappings
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                    "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        # Function to convert numbers below 1000 to words
        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return below_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + helper(num % 10)
            else:
                return below_20[num // 100] + " Hundred " + helper(num % 100)
        
        result = ""
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                result = helper(num % 1000) + unit + " " + result
            num //= 1000
        
        return result.strip()