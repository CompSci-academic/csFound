# Define a class named 'Car'
class Car:
    def __init__(self, make, model):
        # Attributes are marked as private using a single underscore prefix.
        self._make = make
        self._model = model
        # We also initialize an attribute as private, but we don't expose it directly.
        self._mileage = 0

    # Define a method to set the mileage of the car.
    def set_mileage(self, mileage):
        # You can include logic to control the access to attributes.
        if mileage >= 0:
            self._mileage = mileage
        else:
            print("Invalid mileage value")

    # Define a method to get the mileage of the car.
    def get_mileage(self):
        return self._mileage

    # Define a public method to start the car.
    def start(self):
        print(f"The {self._make} {self._model} is starting.")

# Create an instance of the 'Car' class.
my_car = Car("Toyota", "Camry")

# Accessing and modifying private attributes directly is discouraged.
# Instead, we use public methods to interact with them.

# Setting mileage using the public method.
my_car.set_mileage(5000)

# Accessing mileage using the public method.
current_mileage = my_car.get_mileage()
print(f"Current mileage: {current_mileage}")  # Output: Current mileage: 5000

# Attempt to set an invalid mileage (negative value).
my_car.set_mileage(-1000)  # Output: Invalid mileage value

# Start the car using the public method.
my_car.start()  # Output: The Toyota Camry is starting.
