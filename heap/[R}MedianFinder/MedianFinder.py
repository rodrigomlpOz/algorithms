import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for the lower half (invert the numbers for max heap behavior)
        self.lower_half = []
        # Min heap for the upper half
        self.upper_half = []
    
    def add_num(self, num):
        """
        Add a number to the data structure.
        """
        # If lower_half is empty or num is less than or equal to max of lower_half
        if not self.lower_half or num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
            print(f"Added {num} to lower_half: {[-x for x in self.lower_half]}")
        else:
            heapq.heappush(self.upper_half, num)
            print(f"Added {num} to upper_half: {self.upper_half}")
        
        # Balance the heaps if necessary
        if len(self.lower_half) > len(self.upper_half) + 1:
            moved = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, moved)
            print(f"Balanced: Moved {moved} from lower_half to upper_half")
        elif len(self.upper_half) > len(self.lower_half) + 1:
            moved = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -moved)
            print(f"Balanced: Moved {moved} from upper_half to lower_half")
    
    def find_median(self):
        """
        Find and return the median of all elements added so far.
        """
        if len(self.lower_half) > len(self.upper_half):
            median = -self.lower_half[0]
            print(f"Median is the top of lower_half: {median}")
            return median
        elif len(self.upper_half) > len(self.lower_half):
            median = self.upper_half[0]
            print(f"Median is the top of upper_half: {median}")
            return median
        else:
            median = (-self.lower_half[0] + self.upper_half[0]) / 2
            print(f"Median is the average of tops: {median}")
            return median

# Example Usage
if __name__ == "__main__":
    mf = MedianFinder()
    data_stream = [5, 15, 1, 3]
    for num in data_stream:
        mf.add_num(num)
        print(f"Current Median: {mf.find_median()}\n")
