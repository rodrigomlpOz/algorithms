class Vector2D:
    def __init__(self, v):
        self.vector = v
        self.outer = 0
        self.inner = 0
        self.advance_to_next_nonempty()

    def advance_to_next_nonempty(self):
        # This method advances the outer and inner indices to point to the next
        # non-empty sub-list element. If the current sub-list is exhausted or empty,
        # it moves to the next sub-list until it finds a valid position or reaches the end.
        while self.outer < len(self.vector) and self.inner >= len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self):
        # Returns the next element in the 2D vector and advances the indices.
        if not self.hasNext():
            raise Exception("No more elements")
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        self.advance_to_next_nonempty()  # Prepare indices for the next call
        return result

    def hasNext(self):
        # Checks if there are more elements available in the vector.
        # This method ensures that the indices point to a valid element or the end.
        self.advance_to_next_nonempty()
        return self.outer < len(self.vector)

