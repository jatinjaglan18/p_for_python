class Queue:

    def __init__(self):
        self.q =[]
        
        
    def is_empty(self):
        return len(self.q) == 0
    
    def see(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            for i in self.q:
                print(i, end = '->')
            print()

    def peek(self):
        if self.is_empty() :
            print('kuch nhi hai')
        else:
            self.q[0]
    
    def enqueue(self,val):
        self.q.append(val)
    
    def dequeue(self):
        if self.is_empty():
            print('Queue underflow')
        else:
            print(self.q.pop(0))


q = Queue()
q.see()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.see()
q.peek()
q.dequeue()
q.peek()
q.dequeue()
q.peek()
q.dequeue()
q.see()
q.peek()
