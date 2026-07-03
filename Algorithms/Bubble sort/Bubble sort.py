def bubble_sort(arr):
    n = len(arr)
    swapped=False
    for i in range(n):
        for j in range(0, n-1-i):#Reduces the number of comparisons in each iteration as the largest elements are already sorted and placed at the end of the array
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
    if not swapped:
        #Code will return the same array as it is already sorted
        return arr
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort([9, 10, 11, 12, 22, 89, 90])) 