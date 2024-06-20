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

#Stack Using OOPS
class Stack:
    def __init__(self,size):
        self.arr = []
        self.size = size

    def is_empty(self):
        return len(self.arr) == 0
    def get_size(self):    
        return len(self.arr)
    
    def see(self):
        for i in self.arr:
            print(self.arr[-i], end = ' ')
        print()
    
    def peek(self):
        if self.is_empty():
            print( 'Stack is Empty' ) 
        else:
            print( self.arr[-1])

    def push(self,val):
        if self.get_size() == self.size:
            print('Stack Overflow')
        else:
            self.arr.append(val)

    def pop(self):
        if self.is_empty():
            print('Stack Underflow')
        else:
            print(self.arr.pop())
        



stack = Stack(5)
print(stack.size)
stack.push(1)
stack.peek()
stack.push(2)
stack.peek()
stack.push(3)
stack.see()
stack.peek()
stack.pop()
stack.peek()
stack.pop()
stack.peek()
stack.pop()