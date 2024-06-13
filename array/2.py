from array import *

n = int(input())
arr = array('i',[int(input()) for i in range(n)])  
print(arr)

k = int(input())

for i in range(n):
    if arr[i] == k :
        print(i)
        break
else:
    print(-1)



