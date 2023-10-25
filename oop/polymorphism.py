# Base class 'Animal' with a 'speak' method.
class Animal:
    def speak(self):
        pass

# Derived class 'Dog' that inherits from 'Animal'.
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class 'Cat' that inherits from 'Animal'.
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Derived class 'Duck' that inherits from 'Animal'.
class Duck(Animal):
    def speak(self):
        return "Quack!"

# Function that takes any 'Animal' object and makes it speak.
def make_animal_speak(animal):
    return animal.speak()

# Create instances of different animals.
dog = Dog()
cat = Cat()
duck = Duck()

# Call the 'make_animal_speak' function on different animal objects.
print(make_animal_speak(dog))   # Output: Woof!
print(make_animal_speak(cat))   # Output: Meow!
print(make_animal_speak(duck))  # Output: Quack!
