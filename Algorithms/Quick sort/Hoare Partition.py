def hoare_partition(arr, low, high):
    pivot = arr[low]

    i = low - 1
    j = high + 1

    while True:
        # Move i to the right
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move j to the left
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers cross, return the partition index
        if i >= j:
            return j

        # Swap misplaced elements
        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, low, high):
    if low < high:
        # Partition the array
        p = hoare_partition(arr, low, high)

        # Recursively sort the left partition
        quicksort(arr, low, p)

        # Recursively sort the right partition
        quicksort(arr, p + 1, high)


arr = [8, 3, 1, 7, 0, 10, 2]

quicksort(arr, 0, len(arr) - 1)

print(arr)