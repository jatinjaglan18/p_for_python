# span of an array
from array import *

n = int(input())
arr = array('i',[0 for i in range(n)])  #arr = array('i')
print(arr)
for i in range(n):
    j = int(input())    
    arr[i] = j                          #arr.append(j)

l = arr[0]
s = arr[0]
for i in range(1,n):
    if arr[i] > l:
        l = arr[i]
    if arr[i] < s:
        s = arr[i]

print(l-s)
