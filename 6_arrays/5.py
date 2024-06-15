#Difference of two numbers given as an array

from array import *
n1 = int(input())
arr1 = array('i', [int(input()) for i in range(n1)])

n2 = int(input())
arr2 = array('i', [int(input()) for i in range(n2)])    

diff_arr = array('i', [0 for i in range(len(arr2))])

i = len(arr1) - 1
j = len(arr2) - 1
k = len(diff_arr) - 1

c = 0
while k >= 0 :
    d = arr2[j] + c

    if i >= 0:
        if d < arr1[i] :
            d += 10
            num = d - arr1[i]
            diff_arr[k] = num
            c = -1
        else:
            num = d - arr1[i]
            diff_arr[k] = num
            c = 0

    else:
        if d < 0 :
            d += 10
            num = d - 0
            diff_arr[k] = num
            c = -1
        else: 
            num = d - 0
            diff_arr[k] = num
            c = 0
    
    i -= 1
    j -= 1
    k -= 1

idx = 0
while idx < len(diff_arr):
    if diff_arr[idx] == 0:
        idx += 1
    else:
        break

for i in range(idx,len(diff_arr)):
    print(diff_arr[i])
