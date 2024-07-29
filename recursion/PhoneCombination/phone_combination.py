'''
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
'''

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def backtrack(result, temp, dic, digits, index):
            if len(temp) == len(digits):
                result.append(''.join(temp[:]))
            else:
                for char in dic[digits[index]]:
                    #choose
                    temp.append(char)

                    #explore
                    backtrack(result, temp, dic, digits, index + 1)

                    #undo
                    temp.pop()
        if not digits:
            return []
        dic = {"0":"0", "1":"1", "2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        backtrack(result, [], dic, digits, 0)
        return result

