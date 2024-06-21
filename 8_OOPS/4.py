#Linked List

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

    def see(self):
        print(self.data, '/', self.next)        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head == None
    
    def addLast(self,val):
        node = Node(val)        #data = val , next = None

        if self.is_empty():
            self.head = self.tail = node

        else:
            #for 2nd element add -> head.next -> new_node
            self.tail.next = node   # 
            self.tail = node        #tail = Node
            
        self.size += 1

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def get_size(self):
        print(self.size)
        
    def removeFirst(self):
        if self.size == 0:
            print('Linked List is empty')
        elif self.size == 1:
            self.head = None
            self.size = 0
        else:
            self.head = self.head.next
            self.size -= 1

            
    def first(self):
        if self.size == 0:
            print('Linked List is empty')
        else:
            print(self.head.data)

    def last(self):
        if self.size == 0:
            print('Linked List is empty')
        else:
            print(self.tail.data)

    def idx(self,i):
        if i < 0 or i >= self.size:
            print('Aukaat se bhar jaa rhaa h')
        else:
            temp = self.head
            for i in range(i):
                temp = temp.next
            print(temp.data)

    def addFirst(self,val):
        if self.size == 0:
            self.addLast(val)
        else:
            node = Node(val)
            node.next = self.head
            self.head = node
            self.size += 1
    
    def add_at_idx(self,idx,val):
        if idx == 0:
            self.addFirst(val)
        elif idx < 0 or idx > self.size:
            print('Aukat me rhe')
        elif idx == self.size:
            self.addLast(val)
        else:
            node = Node(val)
            temp = self.head
            for i in range(idx-1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
            self.size += 1

    def removeLast(self):
        if self.size == 0:
            print('Linked List is empty')
        elif self.size == 1:
            self.head = None
            self.size = 0
        else:
            temp = self.head
            for i in range(self.size - 2):
                temp = temp.next
            temp.next = None
            self.tail = temp
            self.size -= 1

    def remove_at_idx(self,idx):
        if self.size == 0 or idx >= self.size:
            print('Tera Dimaag Khrab hai')
        
        elif idx == 0:
            self.removeFirst()

        elif idx == self.size - 1:
            self.removeLast()
        else:
            temp = self.head
            for i in range(idx-1):
                temp = temp.next
            temp.next = temp.next.next
            self.size -= 1

    def reverse(Self):

        temp = Self.head
        stack = []
        while temp != None:
            stack.append(temp.data)
            temp = temp.next

        while len(stack) != 0:
            print(stack[-1], end = ' ')
            stack.pop()
