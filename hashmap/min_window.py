    def minWindow(self, s: str, t: str) -> str:
        dic = collections.defaultdict(int)
        for i in range(len(t)):
            dic[t[i]] += 1

        left = 0
        right = 0
        count = 0
        ans = ""
        min_size = float('inf')
        
        while right < len(s):
            if dic[s[right]] > 0:
                    count += 1
            dic[s[right]] -= 1
            while left < len(s) and count == len(t):
                if (right - left + 1) < min_size:
                    min_size = right - left + 1
                    ans = s[left:right+1]
                dic[s[left]] += 1
                if dic[s[left]] > 0:
                    count -= 1
                left += 1
            right += 1

        return ans