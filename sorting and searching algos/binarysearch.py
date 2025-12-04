from bubblesort import bubblesort

b = [35,3,6,45,3,67,7,12,7,56,8,8,3,45,6,7,87,345653,43,4,23,78,55,64,3]
b = bubblesort(b)

def binarysearch(arr, tgt):
    u = len(arr) - 1
    l = 0
    while l <= u:
        mid = (u+l) // 2
        if arr[mid] == tgt:
            return mid
        elif arr[mid] > tgt:
            u = mid - 1
        elif arr[mid] < tgt:
            l = mid + 1
    return -1

print(binarysearch(b,4))