#Generic Tree

class Node:
    def __init__(self,val):
        self.data = val
        self.children = []

arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,150,-1,-1,-1]
sarr = [10,20,-1,30,50,-1,60,-1,-1,40,-1,-1]
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
#print(size(a))


def max_val(node):
    m = float('-inf')

    for i in node.children:
        im = max_val(i)
        m = max(im,m)
    
    m = max(node.data,m)
    return m

#print(max_val(a))

def height(node):
    m = -1      #0 for node, -1 for edges

    for i in node.children:
        ch = height(i)
        m = max(m,ch)

    m += 1
    return m

#print(height(a))
    
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

#level_order_traversal(a)

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

#line_wise(a)

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
        
            

#line_wise(a)
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

def mirror_tree(node):
    
    for i in node.children:
        mirror_tree(i)
    node.children.reverse()

#mirror_tree(a)
#display(a)

def remove_leaves(node):
    for i in range(len(node.children)-1,-1,-1):
        child = node.children[i]
        if len(child.children) == 0:
            node.children.remove(child)
    
    for i in node.children:
        remove_leaves(i)
    
#remove_leaves(a)
#display(a)
def getTail(node):
    while len(node.children) == 1:
        node = node.children[0]
    return node

def linearize(node):
    for i in node.children:
        linearize(i)

    while len(node.children) > 1:
        v = node.children.pop()
        a = getTail(node.children[-1])
        a.children.append(v)

#linearize(a)
#display(a)
    
def find(node,x):
    if node.data == x:
        return True
    for i in node.children:
        flag = find(i,x)
        if flag:
            return True
    return False    

#print(find(a,99))

def node_to_root(node,x):
    if node.data == x:
        arr = [node.data]
        return arr
    for i in node.children:
        a = node_to_root(i,x)
        if len(a) > 0:
            a.append(node.data)
            return a

    return []

#print(node_to_root(a,110))

def lowest_common(node,x,y):
    a1 = node_to_root(node,x)
    a2 = node_to_root(node,y)
    
    i = len(a1)-1
    j = len(a2)-1

    while i >= 0 and j >= 0 and a1[i] == a2[j]:
       i -= 1
       j -= 1
        
    return a1[i+1]
        
print(lowest_common(a,40,20))

def distance(node,x,y):
    a1= node_to_root(node,x)
    a2 = node_to_root(node,y)
    i = len(a1)-1
    j = len(a2)-1

    while i >= 0 and j >= 0 and a1[i] == a2[j]:
       i -= 1
       j -= 1

    i += 1
    j += 1
    '''path = 0
    while i >= 0:
        path += 1
        i -= 1
    
    while j >= 0:
        path += 1
        j -= 1'''
    
    return i + j

#print(distance(a,50,150))

def same_shape(node1, node2):
    if len(node1.children) != len(node2.children):
        return False
    else:
        for i in range(len(node1.children)):
            flag = same_shape(node1.children[i],node2.children[i])
            if flag == False:
                return False
    return True


def ismirror(node1,node2):
    if len(node1.children) != len(node2.children):
        return False
    else:
        for i in range(len(node1.children)):
            j = len(node2.children) -1 - i

            flag = ismirror(node1.children[i],node2.children[j])
            if flag == False:
                return False
            
        return True
    
c = genrateTree(arr)
mirror_tree(c)
display(c)
print(ismirror(a,c))