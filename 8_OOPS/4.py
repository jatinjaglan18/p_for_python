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

def k_reverse(l,k):
    p = LinkedList()
    c = LinkedList()
    s = l.size
    while s >= k:
        for i in range(k):
            c.addFirst(l.head.data)
            l.removeFirst()
            s -= 1
        if p.is_empty():
            p = c
        else:
            p.tail.next = c.head
            p.tail = c.tail
        p.size += k
        c = LinkedList()
    while s != 0:
        p.addLast(l.head.data)
        l.removeFirst()
        s -= 1
    return p

#Iterative approach only data
def diplay_reverse(l):
    stack = []
    temp = l.head
    while temp != None:
        stack.append(temp.data)
        temp = temp.next
    while len(stack) != 0:
        print(stack.pop(), end = ' ')
    print()

#Recursive approach only data
def d_r(h):
    if h.next == None:
        bres = [h.data]
        return bres
    res = []
    l = d_r(h.next)
    res.append(h.data)
    for i in l:
        res.append(i)
    return res

def diplay_revers_recursive(l):
    res = d_r(l.head)
    for i in res:
        print(i,end =' ')

#Reverse LinkedList
def R_l_r(h):
    if h.next == None:
        return
    R_l_r(h.next)
    h.next.next = h

def reverse_Linked_list(l):
    R_l_r(l.head)
    l.head.next = None
    l.tail,l.head = l.head, l.tail

l= LinkedList()

l.addLast(1)
l.addLast(2)
l.addLast(3)
l.addLast(4)
l.addLast(5)
l.addLast(6)
l.display()


def reverse_list(l):
    global left
    left = l.head
    r_help(l.head,0)

def r_help(right,floor):
    if right == None:
        return
    
    global left
    r_help(right.next,floor+1)
    
    if floor >= l.size // 2:
        temp = left.data
        left.data = right.data 
        right.data = temp
        left = left.next
    

def palindrome(l):
    global left
    left = l.head
    return palindrome_helper(l.head)

def palindrome_helper(right):
    if right == None:
        return True
    
    global left
    res = palindrome_helper(right.next)
    
    if left.data != right.data:
        res = False
        return res
    else:
        left = left.next
    return res
    


def fold(l):
    global left
    left = l.head
    fold_helper(l.head,0)

def fold_helper(right,floor):
    if right == None:
        return
    
    global left
    fold_helper(right.next,floor+1)
    if floor > l.size // 2:
        new_node = right
        new_node.next = left.next
        left.next = new_node
        left = new_node.next
    elif floor == l.size // 2:
        l.tail = right
        l.tail.next = None
        

def add_two_linkedlist(l1,l2):
    l = LinkedList()
    oc = helper(l1.head,l2.head,l1.size,l2.size,l)
    if oc != 0:
        l.addFirst(oc)
    return l

def helper(h1,h2,p1,p2,l):
    if h1 == None and h2 == None:
        return 0
    if p1 == p2:
        oc = helper(h1.next,h2.next,p1-1,p2-1,l)
        val = h1.data + h2.data + oc
        c = val // 10 
        a_val = val % 10
        l.addFirst(a_val)
        return c
    
    elif p1 > p2:
        oc = helper(h1.next,h2,p1-1,p2,l)
        val = h1.data + oc
        c = val // 10 
        a_val = val % 10
        l.addFirst(a_val)
        return c 

    elif p2 > p1:
        oc = helper(h1,h2.next,p1,p2-1,l)
        val = h2.data + oc
        c = val // 10 
        a_val = val % 10
        l.addFirst(a_val)
        return c 

    


l1 = LinkedList()
l1.addLast(8)
l1.addLast(1)
l1.display()
l2 = LinkedList()
l2.addLast(9)
l2.addLast(9)
z = add_two_linkedlist(l1,l2)
z.display()