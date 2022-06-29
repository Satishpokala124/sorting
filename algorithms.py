
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] = arr[j] + arr[j+1]
                arr[j+1] = arr[j] - arr[j+1]
                arr[j] = arr[j] - arr[j+1]
    return arr


def merge(arr1, arr2):
    arr = []
    i = 0
    j = 0
    n1 = len(arr1)
    n2 = len(arr2)
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < n1:
        arr.append(arr1[i])
        i += 1
    while j < n2:
        arr.append(arr2[j])
        j += 1
    return arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    arr1 = arr[:middle]
    arr2 = arr[middle:]
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)
    arr = merge(arr1, arr2)
    return arr


def quick_sort(array):
    N = len(array)
    if N <= 1:
        return array
    left, right = 0, N-1
    pivot = array[-1]
    while left < right:
        if array[left] <= pivot:
            left += 1
        else:
            array[left], array[right-1] = array[right-1], array[left]
            array[right-1], array[right] = array[right], array[right-1]
            right -= 1
    array = quick_sort(array[:right]) + [pivot] + quick_sort(array[right+1:])
    return array
