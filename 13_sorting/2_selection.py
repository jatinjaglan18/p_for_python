#selection sort
s = int(input())
arr = [int(input()) for i in range(s)]

def selection_sort(arr):
    for i in range(len(arr)):
        pot = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j] < pot:
                pot = arr[j]
                arr[i],arr[j] = arr[j],arr[i]

selection_sort(arr)
print(arr)