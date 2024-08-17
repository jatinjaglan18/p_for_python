#bubble sort
s = int(input())
arr = [int(input()) for i in range(s)]

def bubble_sort(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)-1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
        
bubble_sort(arr)
print(arr)
            