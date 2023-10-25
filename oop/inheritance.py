# Parent class (base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass  # This method will be overridden in the child classes

# Child class 1
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the parent class
        super().__init__(name, species="Dog")
        self.breed = breed

    # Override the speak method
    def speak(self):
        return f"{self.name} barks."

# Child class 2
class Cat(Animal):
    def __init__(self, name, color):
        # Call the constructor of the parent class
        super().__init__(name, species="Cat")
        self.color = color

    # Override the speak method
    def speak(self):
        return f"{self.name} meows."

# Create instances of the child classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Gray")

# Use the overridden methods
print(dog.speak())  # Output: Buddy barks.
print(cat.speak())  # Output: Whiskers meows.

# Access attributes from the parent class
print(f"{dog.name} is a {dog.species} of breed {dog.breed}.")  # Output: Buddy is a Dog of breed Golden Retriever.
print(f"{cat.name} is a {cat.species} with {cat.color} fur.")  # Output: Whiskers is a Cat with Gray fur.
