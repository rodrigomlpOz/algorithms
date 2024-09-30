from collections import deque

class QueueMax:
    def __init__(self):
        self.queue = deque()       # Regular queue for enqueue/dequeue
        self.max_queue = deque()   # Deque to store the maximum values

    def enqueue(self, x):
        # Add the element to the regular queue
        self.queue.append(x)
        
        # Remove all elements from the back of the max_queue that are smaller than the new element
        while self.max_queue and self.max_queue[-1] < x:
            self.max_queue.pop()
        
        # Add the new element to the back of max_queue
        self.max_queue.append(x)

    def dequeue(self):
        # Remove the front element from the regular queue
        if self.queue:
            front = self.queue.popleft()
            
            # If the element being removed is the same as the front of max_queue, remove it from max_queue as well
            if front == self.max_queue[0]:
                self.max_queue.popleft()
    
    def max(self):
        # Return the front element of max_queue, which is the maximum value in the queue
        if self.max_queue:
            return self.max_queue[0]
        return None  # If queue is empty, return None
