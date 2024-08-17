#0-1 sort

s = int(input())
print('Give input as 0,1')
arr = [int(input()) for i in range(s)]

def partioning(arr):
    i = 0 
    j = 0 
    while i < len(arr):
        if arr[i] == 1:
            i += 1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j += 1

partioning(arr)
print(arr)

#0-1-2 sort
s = int(input())
print('Give input as 0,1,2')
arr = [int(input()) for i in range(s)]

def partioning(arr):
    i = 0
    j = 0
    k = 0
    # 0 - j-1 -> 0 ; j - i-1 -> 1 ; i - k-1 -> 2 
    while k < len(arr):
        if arr[k] == 2:
            k += 1
        elif arr[k] == 1:
            arr[i],arr[k] = arr[k],arr[i]
            k += 1
            i += 1
        else:
            arr[j],arr[i] = arr[i],arr[j]
            arr[k],arr[j] = arr[j],arr[k]

            i += 1
            j += 1
            k += 1

#partioning(arr)
print(arr)

def partioning(arr):
    i = 0
    j = 0
    k = len(arr)-1
    # 0 - j-1 -> 0 ; j - i-1 -> 1 ; k - len(arr) -> 2 
    while i < k:
        if arr[i] == 1:
            i += 1
        elif arr[i] == 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
            i += 1
        else:
            arr[i], arr[k] = arr[k],arr[i]
            k -= 1

partioning(arr)
print(arr)