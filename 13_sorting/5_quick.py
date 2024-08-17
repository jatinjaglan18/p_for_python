#Quick sort
s = int(input())
arr = [int(input()) for i in range(s)]
#k = int(input('Pivot Element: '))

'''def partioning(arr,k):
    arr_small_equal = []
    arr_greater = []

    for i in range(len(arr)):
        val = arr.pop()
        if val > k:
            arr_greater.append(val)
        else:
            arr_small_equal.append(val)

    arr = arr_small_equal + arr_greater
    return arr'''

'''def partioning(arr,k):
    i = 0
    j = 0
    while i < len(arr):
        if arr[i] > k:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    return arr'''
#print(partioning(arr,k))

def partioning(arr,k,l,r):
    i = l
    j = l

    while i <= r:
        if arr[i] > k:
            i += 1
        else:
            arr[i] , arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    
    return j - 1

def quick_sort(arr, l, r):
    if l >= r:
        return 
    pivot = arr[r]     #any element of array

    sei = partioning(arr,pivot,l,r)       #sorted element index
    quick_sort(arr,l,sei-1)
    quick_sort(arr,sei+1,r)

quick_sort(arr,0,len(arr)-1)
print(arr)