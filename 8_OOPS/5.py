#Generic Tree

class Node:
    def __init__(self,val):
        self.data = val
        self.children = []

#arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,150,-1,-1,-1]
arr = [10,20,-1,30,50,-1,60,-1,-1,40,-1,-1]
def genrateTree(arr):
    root = Node(None)      
    stack = []
    for i in arr:
        if i == -1:
            stack.pop()
        else:
            new_node = Node(i)
            if len(stack) != 0:
                stack[-1].children.append(new_node)
            else:
                root = new_node
            stack.append(new_node)
    
    return root

def display(node):
    string = str(node.data) + '-->' 
    for i in node.children:
        string = string + ', ' + str(i.data)
    string = string + '.'
    print(string)
    for i in node.children:
        display(i)  

#s = 0
def size(node):
    s  = 0
    #global s   #s  += cs 
    for i in node.children:
        cs = size(i)
        s  += cs
    s += 1
    return s

a = genrateTree(arr)
display(a)
print(size(a))


def max_val(node):
    m = float('-inf')

    for i in node.children:
        im = max_val(i)
        m = max(im,m)
    
    m = max(node.data,m)
    return m

print(max_val(a))

def height(node):
    m = -1      #0 for node, -1 for edges

    for i in node.children:
        ch = height(i)
        m = max(m,ch)

    m += 1
    return m

print(height(a))
    
def traversal(node):

    print('Node Pre',node.data)
    for i in node.children:
        print('Edge Pre', node.data, '--', i.data)
        traversal(i)
        print('Edge Post', node.data, '--', i.data)
    print('Node Post',node.data)

#traversal(a)

def level_order_traversal(node):
    q = [node]
    while len(q) != 0:
        v = q.pop(0)
        print(v.data, end = ' ')
        for i in v.children:
            q.append(i)

level_order_traversal(a)

print()

def line_wise(node):
    q = [node]
    cq = []

    while len(q) != 0 or len(cq) != 0:
        v = q.pop(0)
        print(v.data,end = ' ')
        
        for i in v.children:
            cq.append(i)

        if len(q) == 0 :
            print()
            q = cq
            cq  =[]

line_wise(a)

#Alternate
def line_wise(node):
    q = [node]
    q.append(None)

    while len(q) != 0:
        v = q.pop(0)
        if v != None:
            print(v.data,end=' ')
            for i in v.children:
                q.append(i)
        else:
            if len(q) != 0:
                print()
                q.append(None)
        
            

line_wise(a)
def zig_zag(node):
    s = [node]
    cs =[]
    flag = True
    while len(s) != 0 or len(cs) != 0:
        v = s.pop()
        print(v.data, end=' ')

        if flag:
            for i in v.children:
                cs.append(i)
        else:
            for i in range(len(v.children)-1,-1,-1):
                cs.append(v.children[i])
    

        if len(s) == 0:
            print()
            s= cs
            cs =[]
            if flag:
                flag = False
            else:
                flag = True

#zig_zag(a)

