#ceil and floor
s = int(input())
arr = [int(input()) for i in range(s)]
x = int(input('Find: '))

def ceil_floor(arr,x):
    ceil = float('inf')
    floor = float('-inf')
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if x < arr[mid]:
            ceil = arr[mid]
            right = mid - 1
        
        elif x > arr[mid]:
            floor = arr[mid]
            left = mid + 1
        else:
            ceil = x
            floor = x
            return ceil,floor
    return ceil,floor
ceil , floor = ceil_floor(arr,x)
print('ceil = ', ceil)
print('floor = ', floor)
