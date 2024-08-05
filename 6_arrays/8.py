#subarray
s = int(input())
arr = [int(input()) for i in range(s)]

for i in range(len(arr)):
    for j in range(i,len(arr)):
        for k in range(i,j+1):
            print(arr[k], end = ' ')
        print()
