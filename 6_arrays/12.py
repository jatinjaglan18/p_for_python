s = int(input())
arr = [int(input()) for i in range(s)]
x = int(input('Find: '))

def binarySearch1(arr,x):
    left = 0
    right = len(arr) - 1
    li = 0
    while left <= right:
        mid = ( left + right ) // 2
        if x < arr[mid]:
            right = mid - 1
        elif x > arr[mid]:
            left = mid + 1
        else:
            li = mid
            left = mid + 1
    return li

def binarySearch2(arr,x):
    left = 0
    right = len(arr) - 1
    fi = 0
    while left <= right:
        mid = ( left + right ) // 2
        if x < arr[mid]:
            right = mid - 1
        elif x > arr[mid]:
            left = mid + 1
        else:
            fi = mid
            right = mid - 1
    return fi

print('First Index:', binarySearch2(arr,x))
print('Last Index:', binarySearch1(arr,x))
