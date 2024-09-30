class QueueFromStacks:
    def __init__(self):
        self.stack_in = []   # Stack for enqueue operations
        self.stack_out = []  # Stack for dequeue and peek operations

    def enqueue(self, x):
        # Simply push the element onto the stack_in
        self.stack_in.append(x)

    def dequeue(self):
        # If stack_out is empty, transfer all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # Pop from stack_out, which is the front of the queue
        if self.stack_out:
            return self.stack_out.pop()
        return None  # If both stacks are empty, return None

    def peek(self):
        # If stack_out is empty, transfer elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # Return the top of stack_out without removing it
        if self.stack_out:
            return self.stack_out[-1]
        return None  # If both stacks are empty, return None

    def empty(self):
        # The queue is empty if both stack_in and stack_out are empty
        return not self.stack_in and not self.stack_out
