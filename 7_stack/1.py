#Implementing stack using list
stack =[]
stack.append(1)
print(stack, 'Size:',len(stack), 'Top Element:', stack[len(stack)-1])

stack.append(2)
print(stack, 'Size:',len(stack), 'Top Element:', stack[len(stack)-1])

stack.append(3)
print(stack, 'Size:',len(stack), 'Top Element:', stack[len(stack)-1])

stack.pop()
print(stack, 'Size',len(stack), 'Top Element', stack[len(stack)-1])

stack.pop()
print(stack, 'Size',len(stack), 'Top Element', stack[len(stack)-1])

stack.pop()


#Stack using collections.deque
from collections import deque
stack = deque()

stack.append(1)
print(stack, 'Size:',len(stack), 'Top Element:', stack[len(stack)-1])

stack.append(2)
print(stack, 'Size:',len(stack), 'Top Element:', stack[len(stack)-1])

stack.append(3)
print(stack, 'Size:',len(stack), 'Top Element:', stack[len(stack)-1])

stack.pop()
print(stack, 'Size',len(stack), 'Top Element', stack[len(stack)-1])

stack.pop()
print(stack, 'Size',len(stack), 'Top Element', stack[len(stack)-1])

stack.pop()
