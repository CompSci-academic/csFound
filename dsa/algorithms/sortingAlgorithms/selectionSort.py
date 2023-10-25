def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the current element is the minimum
        min_index = i

        # Find the index of the minimum element in the unsorted part of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array:", arr)
