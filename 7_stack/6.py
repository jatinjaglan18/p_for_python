#Largest area rectangle in Histogram
from array import *
n = int(input())
arr = array('i', [int(input()) for i in range(n)])

rb = array('i', [0 for i in range(len(arr))])
rb[len(arr)-1] = len(arr)

stack = []
stack.append(len(arr) - 1)


for i in range(len(arr)-2,-1,-1):
    while arr[i] <= arr[stack[len(stack) - 1]]:
        stack.pop()

        if len(stack) == 0:
            rb[i] = len(arr)
            stack.append(i)
            break
    else:
        rb[i] = stack[len(stack) - 1]
        stack.append(i)


lb = array('i', [0 for i in range(len(arr))])
lb[0] = -1
stack =[]
stack.append(0)

for i in range(1,len(arr)):
    while arr[i] <= arr[stack[len(stack) - 1]]:
        stack.pop()

        if len(stack) == 0:
            lb[i] = -1
            stack.append(i)
            break
    else:
        lb[i] = stack[len(stack) - 1]
        stack.append(i)


max_area = 0
for i in range(len(arr)):
    width = rb[i] - lb[i] -1
    area = width * arr[i]
    if max_area < area:
        max_area = area

print(max_area)
