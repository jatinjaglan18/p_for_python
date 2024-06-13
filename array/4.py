#Sum of two array

from array import *
n1 = int(input())
arr1 = array('i', [int(input()) for i in range(n1)])

n2 = int(input())
arr2 = array('i', [int(input()) for i in range(n2)])

arr = arr1

if len(arr2) > len(arr1):
    arr = arr2
    arr2 = arr1

i = 0
j = 0

while i < len(arr) or j < len(arr2):
    if i < len(arr) - len(arr2):
        print(arr[i])
        i += 1
    else:
        print(arr[i] + arr2[j])
        i += 1
        j += 1
