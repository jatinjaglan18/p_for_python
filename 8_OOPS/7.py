#Binary Tree --> At most 2 Childs

class Node:
    def __init__(self,data = None,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

arr = [50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]

def generateBinaryTree(arr):
    stack = []
    root = Node(arr[0])
    stack.append([root,1]) #node, state

    idx = 0
    while len(stack) > 0:
        top = stack[-1]
        if top[1] == 1:
            #left child
            idx += 1
            if arr[idx] != None:
                new_node = Node(arr[idx])
                top[0].left = new_node
                top[1] += 1
                stack.append([new_node,1])
            else:
                top[1] += 1
        elif top[1] == 2:
            #right child
            idx += 1
            if arr[idx] != None:
                new_node = Node(arr[idx])
                top[0].right = new_node
                top[1] += 1
                stack.append([new_node,1])
            else:
                top[1] += 1
            
        else:
            stack.pop()
    
    return root

a = generateBinaryTree(arr)

def display(node):
    if node == None:
        return 
    l = '.' if node.left == None else str(node.left.data)
    '''if node.left == None:
        l = '.'
    else:
        l = str(node.left.data)'''
    
    r  = '.' if node.right == None else str(node.right.data)
    '''if node.right == None:
        r = '.'
    else:
        r = str(node.right.data)'''

    print(l + ' <-', node.data, '-> ' + r)

    display(node.left)
    display(node.right)

display(a)

def size(node):
    if node == None:
        return 0
    ls = size(node.left)
    rs = size(node.right)
    s = ls + rs + 1
    return s 
#print(size(a))

def total_sum(node):
    if node == None:
        return 0
    ls = total_sum(node.left)
    rs = total_sum(node.right)
    s = ls + rs + node.data
    return s
#print(total_sum(a))

def max_val(node):
    #m = float('-inf')
    if node == None:
        return float('-inf')

    lm = max_val(node.left)
    rm = max_val(node.right)
    
    m = max(lm,rm,node.data)

    return m

#print(max_val(a))

def height(node):
    if node == None:
        return -1 #-1 for edeges 0 for nodes 
    
    lh = height(node.left)
    rh = height(node.right)

    ht = max(lh,rh) + 1

    return ht

#print(height(a))

#recursive pre, in, post order
pre = []
In = []
post = []
def pre_in_post(node):
    global pre
    global In
    global post
    if node == None:
        return
    
    pre.append(node.data)
    pre_in_post(node.left)
    In.append(node.data)
    pre_in_post(node.right)
    post.append(node.data)

'''pre_in_post(a)
print(pre)
print(In)
print(post)'''

#iterative pre, in, post
def pre_in_post_iter(node):
    pre = ''
    In = ''
    post = ''

    stack = []
    stack.append([node,-1])

    while len(stack) != 0:
        top = stack[-1]
        if top[1] == -1:
            pre += str(top[0].data) + ' '
            top[1] += 1
            if top[0].left != None:
                stack.append([top[0].left, -1])
        elif top[1] == 0:
            In += str(top[0].data) + ' '
            top[1] += 1
            if top[0].right != None:
                stack.append([top[0].right, -1])
        else:
            post += str(top[0].data) + ' '
            stack.pop()
            
    return pre, In, post

'''pre, In , post = pre_in_post_iter(a)
print(pre)
print(In)
print(post)'''

def level_order_travarsal(node):
    q = [node]
    cq = []
    while len(q) != 0 or len(cq) != 0:
        v = q.pop(0)
        print(v.data, end = ' ')
        if v.left != None:
            cq.append(v.left)
        if v.right != None:
            cq.append(v.right)

        if len(q) == 0:
            print()
            q = cq
            cq = [] 

#Alternate
def level_order_travarsal(node):
    q = [node]
    while q:
        s = len(q)
        for i in range(s):
            v = q.pop(0)
            print(v.data, end = ' ')
            if v.left != None:
                q.append(v.left)
            if v.right != None:
                q.append(v.right)

        print()

level_order_travarsal(a)