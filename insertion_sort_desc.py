def insertion_sort_desc(arr):
    """
    Insertion Sort Algorithm (Monotonically Decreasing Order)

    This implementation is based on the insertion sort algorithm
    described in Chapter 2 of "Introduction to Algorithms" by
    Cormen et al., with the comparison reversed to sort in
    decreasing order instead of increasing.
    """

    # Start from the second element because the first element
    # is already considered sorted
    for i in range(1, len(arr)):
        key = arr[i]          # Element to be inserted
        j = i - 1             # Index of previous element

        # Move elements that are smaller than key
        # one position to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at its correct position
        arr[j + 1] = key


if __name__ == "__main__":
    # Example input array
    data = [5, 2, 9, 1, 5, 6]

    print("Original array:", data)

    # Sort the array in decreasing order
    insertion_sort_desc(data)

    print("Sorted array (decreasing):", data)
