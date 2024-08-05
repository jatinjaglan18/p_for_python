#Binary search
s = int(input())
arr = [int(input()) for i in range(s)]
x = int(input('Find: '))
def binarySearch(arr,x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = ( left + right ) // 2
        if x < arr[mid]:
            right = mid - 1
        elif x > arr[mid]:
            left = mid + 1
        else:
            return mid
    
    return -1
print(binarySearch(arr,x))