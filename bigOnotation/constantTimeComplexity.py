# This function returns the first element of a list.
# Regardless of the list's size, it always takes the same amount of time,
# making it O(1) or constant time complexity.
def get_first_element(arr):
    # Accessing the first element of the list directly.
    # It does not depend on the list's size, so it's constant time.
    return arr[0]

# Example usage
my_list = [10, 20, 30, 40, 50]

# Calling the function with a list of any size
first_element = get_first_element(my_list)

# Printing the result
print("The first element of the list is:", first_element)
