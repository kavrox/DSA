arr = [5,4,3,2,1,1,2,3,4,5]

for i in range(len(arr)-1):
    for j in range(1,len(arr)):
        if arr[j-1] > arr [j]:
            arr[j-1],arr[j] = arr[j], arr[j-1]
print(arr)