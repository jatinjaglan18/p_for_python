#insertion sort
s = int(input())
arr = [int(input()) for i in range(s)]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break

insertion_sort(arr)
print(arr)
