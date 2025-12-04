arr = [5,4,3,2,1,1,2,3,4,5]

def linearsearch(arr,tgt):
    for i in range(len(arr)):
        if arr[i] == tgt:
            return i
    return -1