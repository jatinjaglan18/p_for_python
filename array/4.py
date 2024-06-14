#Sum of two numbers given as an array

from array import *
n1 = int(input())
arr1 = array('i', [int(input()) for i in range(n1)])

n2 = int(input())
arr2 = array('i', [int(input()) for i in range(n2)])

arr = arr1

if len(arr2) > len(arr1):
    arr = arr2
    arr2 = arr1

'''
#Element wise sum of two arrays
i = 0
j = 0

while i < len(arr) or j < len(arr2):
    if i < len(arr) - len(arr2):
        print(arr[i])
        i += 1
    else:
        print(arr[i] + arr2[j])
        i += 1
        j += 1'''

sum_arr = array('i',[0 for i in range(len(arr))])       #array('i')

i = len(arr) - 1
j = len(arr2) - 1
k = len(sum_arr) -1

c = 0

while k >= 0:
    d = c
    if i >= 0 :
        d += arr[i]
    if j >= 0:
        d += arr2[j]
    
    c = d // 10
    d = d % 10

    sum_arr[k] = d                           #array.append(d)

    i -= 1
    j -= 1
    k -= 1
    

if c != 0:
    print(c)

for i in range(len(sum_arr)):                #(len(sum_arr)-1,-1,-1)
    print(sum_arr[i])

