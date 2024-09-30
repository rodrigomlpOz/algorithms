class MaxStack:
    def __init__(self):
        # Single stack to store (element, current_max)
        self.stack = []

    def push(self, val: int) -> None:
        # If the stack is empty, the max is the value itself
        current_max = val if not self.stack else max(val, self.stack[-1][1])
        # Push the value along with the current max
        self.stack.append((val, current_max))

    def pop(self) -> int:
        # Pop the element and return only the value
        return self.stack.pop()[0]

    def top(self) -> int:
        # Return the top element of the stack (just the value part)
        return self.stack[-1][0]

    def getMax(self) -> int:
        # Return the maximum element (the max part of the tuple)
        return self.stack[-1][1]
