#Bar Chart
from array import *

n = int(input())
arr = array('i',[int(input()) for i in range(n)])

m  = arr[0]
for i in range(1,n):
    if arr[i] > m:
        m = arr[i]

for i in range(m):
    for j in range(len(arr)):
        if (m-i) - arr[j] <= 0:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()

