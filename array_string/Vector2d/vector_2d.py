class Vector2D:
    def __init__(self, matrix):
        """
        Initializes the Vector2D with a 2D vector (list of lists).
        
        Args:
            matrix (List[List[int]]): The 2D vector to iterate over.
        """
        self.matrix = matrix      # The 2D vector to iterate
        self.row = 0              # Index for the current row (outer list)
        self.col = 0              # Index for the current column (inner list)
        self._move_to_next_available()

    def _move_to_next_available(self):
        """
        Advances the row and column indices to point to the next available element.
        Skips any empty sublists or exhausted rows.
        """
        while self.row < len(self.matrix):
            # Check if the current row has elements remaining
            if self.col < len(self.matrix[self.row]):
                break  # Found a valid position
            # Move to the next row
            self.row += 1
            self.col = 0  # Reset column index for the new row

    def next_element(self):
        """
        Returns the next element in the 2D vector and advances the indices.
        
        Returns:
            int: The next integer in the 2D vector.
        
        Raises:
            StopIteration: If there are no more elements to return.
        """
        if not self.has_next():
            raise StopIteration("No more elements")
        
        # Retrieve the current element
        current_value = self.matrix[self.row][self.col]
        self.col += 1  # Move to the next element in the current row
        self._move_to_next_available()  # Prepare indices for the next call
        return current_value

    def has_next(self):
        """
        Checks if there are more elements to iterate over in the 2D vector.
        
        Returns:
            bool: True if there are more elements, False otherwise.
        """
        self._move_to_next_available()  # Ensure indices are at a valid position
        return self.row < len(self.matrix)
