
def palindrome_partitioning(word):
    temp = []
    ans = []
    def is_palindrome(word):
        if word:
            return word == word[::-1]
    def recurse(word, temp, ans):
        if not word:
           ans.append(temp[:])
        for i in range(1, len(word)+1):
            if is_palindrome(word[:i]): 
                temp.append(word[:i])
                
                recurse(word[i:], temp, ans)

                temp.pop()
    recurse(word, temp, ans)
    print(ans)
            

    

word = "aab"
palindrome_partitioning(word)
