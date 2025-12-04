arr =[8,7,9,2,3,1,5,4,6]

# for i in range(len(arr)-1):
#     min_pointer = i
#     for j in range(i+1,len(arr)):
#         if arr[j] < arr[min_pointer]:
#             min_pointer = j
#     arr[i], arr[min_pointer] = arr[min_pointer], arr[i]




def selectionsort(arr):
    for i in range(len(arr)-1):
        cur_min = i
        for j in range(i+1,len(arr)):
            if arr[cur_min] > arr[j]:
                cur_min = j
        arr[cur_min], arr[i] = arr[i], arr[cur_min]
    return arr

print(selectionsort(arr))