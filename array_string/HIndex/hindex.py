def hIndex(self, citations: list[int]) -> int:
    # Sort citations in descending order
    citations.sort(reverse=True)
    
    # Calculate the h-index
    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    
    return h_index