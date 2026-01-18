def insertion_sort_desc(arr):
    """
    Sorts a list in monotonically decreasing order using insertion sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements smaller than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Original:", data)

    insertion_sort_desc(data)
    print("Sorted (decreasing):", data)

