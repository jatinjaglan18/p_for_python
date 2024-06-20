class Stack:
    def __init__(self,size):
        self.arr = []
        self.size = size

    def is_empty(self):
        return len(self.arr) == 0
    def get_size(self):    
        return len(self.arr)
    
    def see(self):
        #LIFO
        for i in range(1, len(self.arr)+1):
            print(self.arr[-i], end = ' ')
        print()
    
    def peek(self):
        if self.is_empty():
            print( 'Stack is Empty' ) 
        else:
            return self.arr[-1]

    def push(self,val):
        self.arr.append(val)

    def pop(self):
        if self.is_empty():
            print('Stack Underflow')
        else:
            self.arr.pop()


    def min_mum(self):
        for i in range(len(self.arr)-1):
            
            a1 = self.arr.pop()
            a2 = self.arr.pop()
            if a1 < a2:
                self.push(a1)
            else:
                self.push(a2)

        print(self.peek())
            
    def mi(self,val):
        if self.is_empty():
            self.push(val)

        elif self.peek() > val:
            self.push(val)



stack1 = Stack(5)
stack1.push(10)
stack1.push(5)
stack1.push(2)
stack1.push(3)
stack1.push(6)
stack1.min_mum()

stack = Stack(5)
stack.mi(10)
stack.mi(5)
stack.mi(2)
stack.mi(3)
stack.mi(6)
print(stack.peek())