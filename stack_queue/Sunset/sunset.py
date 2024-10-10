def examine_buildings_with_sunset(sequence):
    candidates = []  # Store tuples of (id, height)
    
    for building_idx, building_height in enumerate(sequence):
        # Remove candidates that are shorter or equal to the current building
        while candidates and building_height >= candidates[-1][1]:  # Compare height (2nd element)
            candidates.pop()
        # Append the new building as a tuple (index, height)
        candidates.append((building_idx, building_height))
    
    # Return the indices of the buildings in reverse order (as seen from the sunset)
    return [c[0] for c in reversed(candidates)]  # Extract the index (1st element)
