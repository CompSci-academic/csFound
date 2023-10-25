def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid

        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    # Target not found in the array
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
