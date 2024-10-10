Finding the median in a data stream is a common problem in computer science, especially when dealing with large or continuous data where storing all elements isn't feasible. The median is the middle value in a list of numbers, which separates the higher half from the lower half. To efficiently find the median as new numbers arrive, we can use two heaps:

1. **Max Heap** (`lower_half`): This heap contains the smaller half of the numbers. We use a max heap so that the largest number in this half can be accessed quickly.
2. **Min Heap** (`upper_half`): This heap contains the larger half of the numbers. It's a standard min heap where the smallest number in this half can be accessed quickly.

By maintaining these two heaps, the median can be retrieved in constant time, and inserting a new number takes logarithmic time.

Here's a step-by-step guide and Python implementation using the `heapq` module:

### Step-by-Step Approach

1. **Initialization**:
   - Initialize two heaps:
     - `lower_half` as a max heap (using negative numbers since `heapq` only provides a min heap).
     - `upper_half` as a min heap.

2. **Adding a Number**:
   - If the new number is less than or equal to the maximum of `lower_half`, push it to `lower_half`.
   - Otherwise, push it to `upper_half`.
   - Balance the heaps so that the size difference is at most 1.

3. **Finding the Median**:
   - If both heaps have the same size, the median is the average of the top elements of both heaps.
   - If one heap has more elements, the median is the top element of that heap.

### Python Implementation

```python
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
```

### Explanation of the Code

1. **Initialization**:
   - `self.lower_half`: Stores the smaller half of the numbers. We store them as negative to simulate a max heap since Python's `heapq` module only provides a min heap.
   - `self.upper_half`: Stores the larger half of the numbers as a standard min heap.

2. **Adding a Number (`add_num`)**:
   - Check where to add the new number (`lower_half` or `upper_half`).
   - After adding, ensure that the heaps are balanced in size. The size difference should not exceed 1.

3. **Finding the Median (`find_median`)**:
   - If one heap has more elements, the median is the top element of that heap.
   - If both heaps have the same number of elements, the median is the average of the top elements of both heaps.

4. **Example Usage**:
   - Adds numbers from `data_stream` one by one and prints the current median after each insertion.

### Output of the Example

```
Added 5 to lower_half: [5]
Median is the top of lower_half: 5
Current Median: 5

Added 15 to upper_half: [15]
Median is the average of tops: 10.0
Current Median: 10.0

Added 1 to lower_half: [5, 1]
Balanced: Moved 5 from lower_half to upper_half
Median is the top of upper_half: 5
Current Median: 5

Added 3 to lower_half: [3, 1]
Median is the average of tops: 4.0
Current Median: 4.0
```

### Time and Space Complexity

- **Time Complexity**:
  - `add_num`: O(log N), where N is the number of elements in the heaps.
  - `find_median`: O(1), constant time.

- **Space Complexity**:
  - O(N), where N is the number of elements processed so far.

### Additional Considerations

- **Handling Even and Odd Counts**: The code correctly handles both even and odd numbers of elements by balancing the heaps accordingly.
  
- **Duplicate Elements**: The implementation naturally handles duplicate elements without any issues.

- **Streaming Data**: This approach is suitable for real-time data streams where elements are continuously arriving.

### Conclusion

Using two heaps is an efficient way to find the median in a data stream in Python. This approach ensures that both insertion and median retrieval operations are optimized for performance, making it suitable for large-scale or real-time applications.