def validPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
      
        words = [letter for letter in s if letter.isalnum()]
        
        start = 0
        end = len(words) - 1

        while (start < end):
            if words[start].lower() != words[end].lower():
                return False
            start += 1
            end -= 1
        return True