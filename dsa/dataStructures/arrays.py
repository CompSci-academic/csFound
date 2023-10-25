# Initialize lists for your farm
animals = ['cow', 'sheep', 'chicken', 'horse']
vegetables = ['carrot', 'tomato', 'potato', 'lettuce']
fruits = ['apple', 'banana', 'strawberry', 'grape']

# Add an animal to the list
animals.append('goat')

# Remove a vegetable from the list
vegetables.remove('tomato')

# Add a fruit to the list
fruits.append('orange')

# Access specific elements
first_animal = animals[0]
second_vegetable = vegetables[1]
last_fruit = fruits[-1]

print("Animals on the farm:", animals)
print("Vegetables on the farm:", vegetables)
print("Fruits on the farm:", fruits)

print("First animal:", first_animal)
print("Second vegetable:", second_vegetable)
print("Last fruit:", last_fruit)

# Check if elements exist in the lists
if 'chicken' in animals:
    print("There is a chicken on the farm.")
else:
    print("No chicken on the farm.")

if 'apple' in fruits:
    print("There are apples on the farm.")
else:
    print("No apples on the farm.")
