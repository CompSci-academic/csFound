import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def extract_min(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        else:
            return "Heap is empty"

    def is_empty(self):
        return len(self.heap) == 0

# Create a min-heap
min_heap = MinHeap()

# Insert elements into the heap
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(4)
min_heap.insert(2)

# Extract the minimum element from the heap
min_element = min_heap.extract_min()
print("Minimum element:", min_element)

# Check if the heap is empty
if min_heap.is_empty():
    print("The heap is empty.")
else:
    print("The heap is not empty.")
