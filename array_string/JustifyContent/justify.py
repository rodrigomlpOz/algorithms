from typing import List

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    result = []             # To store the final justified text
    current_line = []       # To store words for the current line
    num_of_letters = 0      # Total number of letters in current_line

    for word in words:
        # Check if adding the new word exceeds the maxWidth
        if num_of_letters + len(word) + len(current_line) > maxWidth:
            if len(current_line) == 1:
                # If there's only one word in the line, left-justify it
                line = current_line[0] + ' ' * (maxWidth - num_of_letters)
            else:
                # Calculate the total number of spaces to distribute
                total_spaces = maxWidth - num_of_letters
                space_between_words, extra_spaces = divmod(total_spaces, len(current_line) - 1)
                
                line = ''
                for i in range(len(current_line) - 1):
                    # Assign an extra space to the left slots
                    spaces_to_add = space_between_words + (1 if i < extra_spaces else 0)
                    line += current_line[i] + ' ' * spaces_to_add
                line += current_line[-1]  # Add the last word without extra spaces
            result.append(line)
            # Reset for the next line
            current_line = []
            num_of_letters = 0
        # Add the current word to the line
        current_line.append(word)
        num_of_letters += len(word)
    
    # Handle the last line: left-justified
    last_line = ' '.join(current_line)
    spaces_to_add = maxWidth - len(last_line)
    last_line += ' ' * spaces_to_add
    result.append(last_line)
    
    return result