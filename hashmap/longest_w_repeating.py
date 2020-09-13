import collections
def longest_subs_w_repeating(word):
    left = 0
    right = 0
    max_so_far = 0
    bag = set()
    while right < len(s):
        if s[right] not in bag:
            bag.add(s[right])
            right += 1
            max_so_far = max(max_so_far, right - left)
        else:
            bag.remove(s[left])
            left += 1
    return max_so_far

s = "abcabcbb"
ans = longest_subs_w_repeating(s)
print(ans)