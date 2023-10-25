class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Create a queue
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements from the queue
dequeued_element = queue.dequeue()
print("Dequeued element:", dequeued_element)

# Check if the queue is empty
if queue.is_empty():
    print("The queue is empty.")
else:
    print("The queue is not empty.")

# Get the size of the queue
queue_size = queue.size()
print("Queue size:", queue_size)
