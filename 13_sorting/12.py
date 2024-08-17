#Pivot of sorted rotated array

s = int(input())
arr = [int(input()) for i in range(s)]

def findPivot(arr):
    l = 0
    r = len(arr)-1

    while l < r:
        mid = (l + r) // 2

        # mid -> end = increase
        if arr[mid] < arr[r]:
            r = mid
        
        # mid -> end = decrease
        elif arr[mid] > arr[r]:
            l = mid + 1
    
    return arr[l]       # l == r - > pivot

    
print(findPivot(arr))