class Vector2D:
    def __init__(self, v):
        self.v = v  # The 2D vector
        self.row = 0  # Current row index
        self.col = 0  # Current column index within the row
        self._advance_to_next()  # Move to the first valid element

    def _advance_to_next(self):
        # Advance indices to the next available element
        while self.row < len(self.v) and self.col >= len(self.v[self.row]):
            self.row += 1  # Move to the next row
            self.col = 0   # Reset column index to the start

    def next(self):
        if not self.hasNext():
            raise StopIteration("No more elements in the vector.")
        result = self.v[self.row][self.col]  # Get the current element
        self.col += 1  # Move to the next column
        self._advance_to_next()  # Prepare for the next call
        return result

    def hasNext(self):
        # Check if there are any elements left
        return self.row < len(self.v)
