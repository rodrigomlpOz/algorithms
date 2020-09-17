def myAtoi(str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        sign = 1 
        if not str or str[0].isalpha():
            return 0
        else:
            if str[0] == "+":
                str = str[1:]
            elif str[0] == "-":
                str = str[1:]
                sign = -1
            num = 0 
            i = 0
            while i < len(str) and str[i].isdigit():
                    num = num * 10 + (ord(str[i])-ord('0'))
                    i += 1
            return max(-2**31, min(sign * num,2**31-1))