# This function searches for a target element in a list.
# The time it takes to find the target element grows linearly with the list size, making it O(n).
def linear_search(arr, target):
    for element in arr:
        # Comparing the current element with the target element.
        if element == target:
            return True
    # If the target element is not found after checking all elements, return False.
    return False

# Example usage
my_list = [10, 20, 30, 40, 50]
target_element = 30

# Calling the function with the list and target element
result = linear_search(my_list, target_element)

# Printing the result
if result:
    print(f"The target element {target_element} was found in the list.")
else:
    print(f"The target element {target_element} was not found in the list.")
