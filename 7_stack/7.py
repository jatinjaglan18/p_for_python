#Sliding Window Maximum
from array import *
n = int(input())
arr = array('i', [int(input()) for i in range(n)])

k = int(input('k: '))

#Brute Force
res = []

for i in range(len(arr)-k+1):
    e = arr[i]
    j = i
    while j < i+k:
        if e < arr[j]:
            e = arr[j]
        j+=1
    res.append(e)

print(res)


#o(n)
stack = []
stack.append(len(arr)-1)

res = array('i', [0 for i in range(len(arr))])

res[len(res)-1] = len(arr)

for i in range(len(arr)-2, -1, -1):
    while arr[stack[-1]] < arr[i]:
        stack.pop()

        if len(stack) == 0:
            res[i] = len(arr)
            break
    else:
        res[i] = stack[-1]

    stack.append(i)

j = 0
for i in range(len(arr)-k+1):
    if j < i:
        j = i

    while res[j] < i+k: 
        j = res[j]
         
    print(arr[j])


