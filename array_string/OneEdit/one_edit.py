def isOneEditDistance(self, s: str, t: str) -> bool:
    m, n = len(s), len(t)

    # If the length difference is more than 1, they can't be one edit distance apart
    if abs(m - n) > 1:
        return False

    # Check if the strings are the same length (possible replacement case)
    if m == n:
        count_diff = 0
        for i in range(m):
            if s[i] != t[i]:
                count_diff += 1
            if count_diff > 1:
                return False
        return count_diff == 1

    # Check if one string is longer than the other by exactly 1 (possible insert/delete case)
    if m > n:
        s, t = t, s  # Ensure s is always the shorter one

    # Compare the strings with the possibility of inserting a character
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            # If there is a mismatch, check if skipping the character from the longer string resolves it
            return s[i:] == t[j+1:]
        i += 1
        j += 1

    # If all the previous characters matched, it can only be one edit distance apart
    # if there is exactly one extra character at the end of the longer string
    return True