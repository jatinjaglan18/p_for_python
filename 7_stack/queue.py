#queue using list
q = []
q.append(0)
print(q, 'Size:',len(q), 'Top Element:',q[0])
q.append(1)
print(q, 'Size:',len(q), 'Top Element:',q[0])
q.append(2)
print(q, 'Size:',len(q), 'Top Element:',q[0])

q.pop(0)
print(q, 'Size:',len(q), 'Top Element:',q[0])
q.pop(0)
print(q, 'Size:',len(q), 'Top Element:',q[0])
q.pop(0)

#Queue using collections.deque
from collections import deque
q = deque()
q.append(0)
print(q, 'Size:',len(q), 'Top Element:',q[0])
q.append(1)
print(q, 'Size:',len(q), 'Top Element:',q[0])
q.append(2)
print(q, 'Size:',len(q), 'Top Element:',q[0])

q.popleft()
print(q, 'Size:',len(q), 'Top Element:',q[0])
q.popleft()
print(q, 'Size:',len(q), 'Top Element:',q[0])
q.popleft()

#Queue using OOPS
class Queue:
    def __init__(self,size):
        self.q = []
        self.size = size

    def is_empty(self):
        return len(self.q) == 0
    def get_size(self):
        return len(self.q)

    def peek(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            print(self.q[0])

    def enqueue(self,val):
        if self.get_size() == self.size:
            print('Queue overflow')
        else:
            self.q.append(val)
    
    def dequeue(self):
        if self.is_empty():
            print('Queue underflow')
        else:
            print(self.q.pop(0))
    
    def see(self):
        if self.is_empty():
            print('Empty')
        else:
            for i in self.q:
                print(i,end=' ')
            print()
    
q = Queue(5)
q.see()
q.enqueue(1)
q.enqueue(5)
q.peek()
q.see()
q.dequeue()
q.peek()
q.dequeue()
q.see()