def lomuto_partition(arr,start,end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
def quicksort(arr, start, end):
    if start < end:
        p = lomuto_partition(arr, start, end)
        quicksort(arr, start, p - 1)
        quicksort(arr, p + 1, end)
arr=[8, 3, 1, 7, 0, 10, 2]
quicksort(arr, 0, len(arr) - 1)
print(arr)
