# This function performs a binary search to find the index of a target element in a sorted list.
# It has a time complexity of O(log n) because the list size is halved in each iteration.
def binary_search(arr, target):
    left = 0  # Left boundary of the search range
    right = len(arr) - 1  # Right boundary of the search range

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found; return its index
        elif arr[mid] < target:
            left = mid + 1  # Adjust the left boundary
        else:
            right = mid - 1  # Adjust the right boundary

    return -1  # Target not found in the list

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]

# Calling the binary_search function with the target element 9
index = binary_search(sorted_list, 9)

# Printing the result
if index != -1:
    print(f"Element 9 is found at index {index}.")
else:
    print("Element 9 is not in the list.")
