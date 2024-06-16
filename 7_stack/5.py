#Stock Span
from array import *
n = int(input())
arr = array('i', [int(input()) for i in range(n)])

stack = []
stack.append(0)
res = array('i', [0 for i in range(n)])
res[0] = 1
for i in range(1,len(arr)):
    while arr[stack[len(stack)-1]] < arr[i]:
        stack.pop()

        if len(stack) == 0:
            res[i] = i+1
            stack.append(i)
            break

    else:
        res[i] = i - stack[len(stack)-1]
        stack.append(i)

print(res)
