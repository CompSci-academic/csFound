# Create an empty set
my_set = set()

# Add elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)

# Display the set
print("Set:", my_set)

# Remove an element from the set
my_set.remove(2)

# Display the updated set
print("Updated Set:", my_set)

# Check if an element is in the set
if 3 in my_set:
    print("3 is in the set.")
else:
    print("3 is not in the set.")

# Create another set for set operations
other_set = {3, 4, 5}

# Union of two sets
union_set = my_set.union(other_set)
print("Union:", union_set)

# Intersection of two sets
intersection_set = my_set.intersection(other_set)
print("Intersection:", intersection_set)
