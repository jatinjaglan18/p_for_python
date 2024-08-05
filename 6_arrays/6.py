#Reverse
s = int(input())
arr = [int(input()) for i in range(s)]
def rev(arr):
    i = 0
    j = len(arr)-1

    while i < j :
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

    return arr
#rev(arr)
#print(arr)

r = int(input('Rotations: '))
def rotate(arr,r):
    r = r % len(arr)
    if r < 0:
        r = r + len(arr)

    arr1 = arr[:len(arr) - r]
    arr2 = arr[len(arr)-r:]

    rev(arr1)
    rev(arr2)

    arr = arr1+arr2
    rev(arr)

    return arr

print(rotate(arr,r))