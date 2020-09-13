import collections, string
def group_anagrams(strs):
    dict = collections.defaultdict(list)
    
    for str in strs:
        arr = [0] * 26
        for char in str:
            arr[ord(char) - ord('a')] += 1
        dict[tuple(arr)].append(str)
    return list(dict.values())
    


strs = ["eat","tea","tan","ate","nat","bat"]
ans = group_anagrams(strs)
print(ans)
'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''