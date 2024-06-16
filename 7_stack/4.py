#Next Greater element to the Right
from array import *
n = int(input())
arr = array('i', [int(input()) for i in range(n)])

#Brute Force
for i in range(n):
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            print('NGETR of', arr[i], 'is', arr[j])
            break
    else:
        print('NGETR of', arr[i], 'is', -1)


#o(n)
res = array('i',[0 for i in range(n)])
stack = []
stack.append(arr[n-1])
res[-1] = -1

for i in range(n-2,-1,-1):
    
    while arr[i] >= stack[len(stack)-1]:
        stack.pop()
        if len(stack) == 0:
            res[i] = -1
            break
        
    else:
        res[i] = stack[len(stack)-1]

    stack.append(arr[i])

print(res)

#Alternate 
res = array('i',[0 for i in range(n)])
stack = []
stack.append(0)

for i in range(1,len(arr)):
    while arr[stack[len(stack)-1]] < arr[i]:
        res[stack[len(stack)-1]] = arr[i]
        stack.pop()

        if len(stack) == 0 :
            stack.append(i)
            break
    else:
        stack.append(i)

if len(stack) != 0:
    while len(stack) != 0:
        res[stack[len(stack)-1]] = -1
        stack.pop()

print(res)

for i in range(len(arr)):
    print('NGETR',arr[i], 'is: ', res[i])