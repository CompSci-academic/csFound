class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

# Create a stack
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Peek at the top element
top_element = stack.peek()
print("Top element:", top_element)

# Pop elements from the stack
popped_element = stack.pop()
print("Popped element:", popped_element)

# Check if the stack is empty
if stack.is_empty():
    print("The stack is empty.")
else:
    print("The stack is not empty.")

# Get the size of the stack
stack_size = stack.size()
print("Stack size:", stack_size)
