class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Initialize linked lists for your farm
animal_list = LinkedList()
animal_list.append('cow')
animal_list.append('sheep')
animal_list.append('chicken')
animal_list.append('horse')

vegetable_list = LinkedList()
vegetable_list.append('carrot')
vegetable_list.append('tomato')
vegetable_list.append('potato')
vegetable_list.append('lettuce')

fruit_list = LinkedList()
fruit_list.append('apple')
fruit_list.append('banana')
fruit_list.append('strawberry')
fruit_list.append('grape')

# Add and remove elements from the linked lists
animal_list.append('goat')
vegetable_list.remove('tomato')
fruit_list.append('orange')

# Access specific elements
first_animal = animal_list.display()[0]
second_vegetable = vegetable_list.display()[1]
last_fruit = fruit_list.display()[-1]

print("First animal:", first_animal)
print("Second vegetable:", second_vegetable)
print("Last fruit:", last_fruit)

# Check if elements exist in the linked lists
if 'chicken' in animal_list.display():
    print("There is a chicken on the farm.")
else:
    print("No chicken on the farm.")

if 'apple' in fruit_list.display():
    print("There are apples on the farm.")
else:
    print("No apples on the farm.")

# Display the complete lists of elements
print("Animal List:", animal_list.display())
print("Vegetable List:", vegetable_list.display())
print("Fruit List:", fruit_list.display())