from typing import List

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    result = []             # To store the final justified text
    current_line = []       # Words for the current line
    num_of_letters = 0      # Total number of letters in current_line

    for word in words:
        # Number of spaces between words if we add the new word
        num_spaces_needed = len(current_line)  # After adding the new word
        
        # Check if adding the new word exceeds maxWidth
        # Total length = letters + new word + spaces between words
        if num_of_letters + len(word) + num_spaces_needed > maxWidth:
            if len(current_line) == 1:
                # If only one word, left-justify by adding spaces at the end
                line = current_line[0] + ' ' * (maxWidth - num_of_letters)
            else:
                # Calculate total spaces to distribute
                total_spaces = maxWidth - num_of_letters
                spaces_between_words, extra_spaces = divmod(total_spaces, len(current_line) - 1)
                
                line = ''
                for i in range(len(current_line) - 1):
                    # Distribute extra spaces to the leftmost slots
                    spaces_to_add = spaces_between_words + (1 if i < extra_spaces else 0)
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
    # Pad with spaces at the end if necessary
    last_line += ' ' * (maxWidth - len(last_line))
    result.append(last_line)
    
    return result

# Example usage:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

