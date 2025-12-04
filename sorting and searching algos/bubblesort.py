
def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(1,len(arr)):
            if arr[j-1] > arr [j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
    return arr
