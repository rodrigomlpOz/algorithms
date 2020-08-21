'''
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
def letter_combination(phone):
    letters = {"1":"1", "2":"abc","3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    temp = []
    ans = []
    def recurse(letters, phone, temp, ans, pos):
        if len(temp) == len(phone):
            ans.append(''.join(temp[:]))
        else:
            for letter in letters[phone[pos]]:
                temp.append(letter)

                recurse(letters, phone, temp, ans, pos+1)

                temp.pop()
    recurse(letters, phone, temp, ans, 0)

            

    

phone = "23"
letter_combination(phone)
print('hello')
