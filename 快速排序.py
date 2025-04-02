def partition(arr, start, end):
    partition = arr[start]
    left = start
    right = end
    if start < end:
        while left < right and arr[right] >= partition:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= partition:
            left += 1
        arr[right] = arr[left]
    arr[left] = partition
    return left

def quickSort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quickSort(arr, start, pi-1)
        quickSort(arr, pi+1, end)

arr = [1,7,2,4,9,10,20,3]
quickSort(arr, 0, len(arr)-1)
print(arr)