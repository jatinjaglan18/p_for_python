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

#display reverse contents of array using recursion
def displayr(arr,i):
    if i == len(arr):
        return
    displayr(arr,i+1)
    print(arr[i])

#Maximum of an array
def maxi(arr,i):
    if i == len(arr):
        return len(arr)-1
    ele = maxi(arr,i+1)
    if arr[i] > arr[ele]:
        return i
    else:
        return ele

#Find First ouccurrence of array
def findFirst(arr,i,val):
    if i == len(arr):
        return -1
    if arr[i] == val:
        return i 
    else:
        return findFirst(arr,i+1,val)
        
#Find last ouccurrence of array
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


#Print all indices of a value in an array using insert function
def allIndices(arr,i,val):
    if i == len(arr):
        L = []
        return L

    L = allIndices(arr,i+1,val)
    if arr[i] == val:
        L.insert(0,i)
    return L

#Print all indices of a value in an array without using insert function
def allIndices(arr,i,val,count):
    if i == len(arr):
        arr1 = [0 for i in range(count)]
        return arr1
    
    if arr[i] == val:
        arr1 = allIndices(arr, i+1 , val, count+1)
        arr1[count] = i
        return arr1
    else:
        arr1 = allIndices(arr, i+1, val, count)
        return arr1
