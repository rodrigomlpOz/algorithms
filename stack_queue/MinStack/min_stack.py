class MinStack:
    def __init__(self):
        # Initialize the main stack and a stack to keep track of the minimum values
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # Push the minimum value onto the minStack. If the minStack is empty, push val.
        # Otherwise, push the smaller of the current value and the top of the minStack
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
    
    def pop(self) -> None:
        # Pop the top element from both the main stack and the minStack
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
    
    def top(self) -> int:
        # Return the top element of the main stack
        if self.stack:
            return self.stack[-1]
    
    def getMin(self) -> int:
        # Return the top element of the minStack, which is the current minimum
        if self.minStack:
            return self.minStack[-1]
