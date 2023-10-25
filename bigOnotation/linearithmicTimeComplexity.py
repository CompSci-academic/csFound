# Linearithmic time complexity, represented as O(n log n), is commonly associated with algorithms like merge sort and quicksort.
# This function performs a merge sort on a list of numbers.
# Merge sort is an example of an algorithm with O(n log n) time complexity.
def merge_sort(arr):
    if len(arr) > 1:
        # Divide the list into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call to merge_sort for both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Initialize pointers for traversing the two halves
        i, j, k = 0, 0, 0

        # Merge the two halves back together
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
my_list = [38, 27, 43, 3, 9, 82, 10]

# Sorting the list using merge_sort
merge_sort(my_list)

# Printing the sorted list
print("Sorted list:", my_list)
