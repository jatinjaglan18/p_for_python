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
    
    while arr[i] > stack[len(stack)-1]:
        stack.pop()
        if len(stack) == 0:
            break
        
    if len(stack) == 0:
        res[i] = -1
        
    else:
        res[i] = stack[len(stack)-1]

    stack.append(arr[i])

print(res)