#display contents of array using recursion
from array import *
n = int(input())
arr = array('i',[0 for i in range(n)])

for i in range(len(arr)):
    j = int(input())
    arr[i] = j

def display(arr,i):
    if i == len(arr):
        return
    print(arr[i])
    display(arr,i+1)


def displayr(arr,i):
    if i == len(arr):
        return
    displayr(arr,i+1)
    print(arr[i])



def maxi(arr,i):
    if i == len(arr):
        return len(arr)-1
    ele = maxi(arr,i+1)
    if arr[i] > arr[ele]:
        return i
    else:
        return ele



def findFirst(arr,i,val):
    if i == len(arr):
        return -1
    if arr[i] == val:
        return i 
    else:
        return findFirst(arr,i+1,val)
        

def findLast(arr,i,val):
    if i == len(arr):
        return -1
    ouc = findLast(arr,i+1,val)
    if ouc == -1:
        if arr[i] == val:
            return i
        else:
            return -1
    else: 
        return ouc

print(findLast(arr,0,8))