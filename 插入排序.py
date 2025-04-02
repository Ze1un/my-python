def insetsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1 #未排序的第一个元素
        while j >=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
arr = [2,1,5,6,3,1]
print(insetsort(arr))

