def count_and_say(n: int) -> str:
    # The initial sequence starts with "1"
    current_sequence = "1"
    
    # Build up to the nth term
    for i in range(n - 1):
        next_sequence = ""
        count = 1
        
        # Iterate over the current sequence to form the next sequence
        for j in range(1, len(current_sequence)):
            if current_sequence[j] == current_sequence[j - 1]:
                count += 1
            else:
                next_sequence += str(count) + current_sequence[j - 1]
                count = 1
        
        # Append the last group of counted digits
        next_sequence += str(count) + current_sequence[-1]
        
        # Move to the next sequence
        current_sequence = next_sequence
    
    return current_sequence

# Example usage:
n = 5
print(count_and_say(n))  # Output: "111221"
