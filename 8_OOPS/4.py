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
            return temp.data

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
    
    def get_node(self,idx):
        temp = self.head
        for i in range(idx):
            temp = temp.next
        return temp

    #Reverse linkedlist using node.data
    def reverse(self):
        for i in range((self.size//2)+1):
            v1 = self.get_node(i)
            v2 = self.get_node(self.size - (i+1))
            
            v1.data, v2.data = v2.data, v1.data  #Swap

    #Reverse using node.next pointer
    def reverse1(self):
        temp = self.tail
        for i in range(self.size-1, -1, -1):
            right = self.get_node(i)
            if i != 0:
                left = self.get_node(i-1)
                right.next = left
            else:
                right.next = None
                self.tail = right
        self.head = temp

    def mid(self):
        s = self.head
        f = self.head
        while f.next != None and f.next.next != None:
            s = s.next
            f = f.next.next
        return s.data

class Stack:
    def __init__(self):
        self.s = LinkedList()
        self.size = 0
    
    def get_size(self):
        return self.size
    def peek(self):
        return self.s.tail.data
    
    def push(self,val):
        self.s.addLast(val)
        self.size += 1

    def pop(self):
        #print(self.s.tail.data)
        self.s.removeLast()
        self.size -=1


class Queue:
    def __init__(self):
        self.q = LinkedList()
        self.size = 0
    def get_size(self):
        return self.size
    def peek(self):
        print(self.q.head.data)
    def enqueue(self,val):
        self.q.addLast(val)
        self.size += 1
    def dequeue(self):
        self.q.removeFirst()
        self.size -= 1


def k_from_last(l,k):
    i = l.head
    j = l.head

    for x in range(k):
        j = j.next
    
    while j != l.tail:
        i = i.next
        j = j.next
    
    return i.data

#Using stack
def k_from_last(l,k):
    s = Stack()
    temp = l.head
    while temp != None:
        s.push(temp.data)
        temp = temp.next
    
    for i in range(k):
        s.pop()
    return s.peek()


def MergeSortSort(l1,l2):
    temp1 = l1.head
    temp2 = l2.head

    l = LinkedList()
    while temp1 != None and temp2 != None:
        if temp1.data <= temp2.data:
            l.addLast(temp1.data)
            temp1 = temp1.next
        elif temp2.data < temp1.data:
            l.addLast(temp2.data)
            temp2 = temp2.next
        
        
    while temp1 != None:
            l.addLast(temp1.data)
            temp1 = temp1.next

    while temp2 != None:
            l.addLast(temp2.data)
            temp2 = temp2.next
    return l

def midNode(h,t):               #h = head node, t = tail node
        s = h
        f = s
        while f != t and f.next != t:
            s = s.next
            f = f.next.next
        return s


def MergeSort(h,t):
    if h == t :
        r = LinkedList()
        r.addLast(h.data)
        return r
    
    mid = midNode(h,t)
    fsh = MergeSort(h,mid)
    ssh = MergeSort(mid.next, t)
    res = LinkedList()
    res = MergeSortSort(fsh,ssh)
    return res


l = LinkedList()
l.addLast(1)
l.addLast(2)
l.addLast(5)
l.addLast(6)
l.addLast(7)
l.addLast(11)
l.addLast(13)
l.addLast(12)


l.display()

def remove_duplicates(l):
    i = l.head
    j = l.head.next

    while j != None:
        if i.data == j.data:
            i.next =  j.next
            l.size -= 1
            j = j.next
        else:
            i = i.next
            j = j.next

def odd_even(l):
    temp = l.head
    e = LinkedList()
    o = LinkedList()
    for i in range(l.size):
        if temp.data % 2 == 0:
            e.addLast(temp.data)
        else:
            o.addLast(temp.data)
        temp = temp.next
    
    o.tail.next = e.head
    return o

z = odd_even(l)
z.display()
