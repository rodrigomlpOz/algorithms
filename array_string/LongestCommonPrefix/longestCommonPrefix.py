from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    # Initialize the prefix with the first string
    prefix = strs[0]
    
    for string in strs[1:]:
        # Shorten the prefix until it matches the start of the current string
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix