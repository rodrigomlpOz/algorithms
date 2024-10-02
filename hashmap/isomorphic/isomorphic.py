def isIsomorphic(s: str, t: str) -> bool:
    # Dictionaries to store the character mappings
    map_s_to_t = {}
    map_t_to_s = {}
    
    # Iterate through characters of both strings
    for char_s, char_t in zip(s, t):
        # Check if there is a conflicting mapping from s to t
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        # Check if there is a conflicting mapping from t to s
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        
        # Create the new mappings
        map_s_to_t[char_s] = char_t
        map_t_to_s[char_t] = char_s
    
    return True
