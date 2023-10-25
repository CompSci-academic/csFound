# This function calculates the sum of all pairs of elements in a list.
# The time it takes to complete grows quadratically with the size of the list.
def sum_of_pairs(arr):
    total_sum = 0  # Initialize a variable to store the sum of pairs

    # Nested loops to iterate over all possible pairs of elements in the list
    for i in range(len(arr)):
        for j in range(len(arr)):
            total_sum += arr[i] + arr[j]  # Add the sum of the pair to the total_sum

    return total_sum

# Example usage
my_list = [1, 2, 3, 4]

# Calling the function with a list of size n
result = sum_of_pairs(my_list)

# Printing the result
print("The sum of all pairs is:", result)
