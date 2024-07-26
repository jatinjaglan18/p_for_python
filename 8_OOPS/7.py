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
print(size(a))

def total_sum(node):
    if node == None:
        return 0
    ls = total_sum(node.left)
    rs = total_sum(node.right)
    s = ls + rs + node.data
    return s
print(total_sum(a))

def max_val(node):
    #m = float('-inf')
    if node == None:
        return float('-inf')

    lm = max_val(node.left)
    rm = max_val(node.right)
    
    m = max(lm,rm,node.data)

    return m

print(max_val(a))

def height(node):
    if node == None:
        return -1 #-1 for edeges 0 for nodes 
    
    lh = height(node.left)
    rh = height(node.right)

    ht = max(lh,rh) + 1

    return ht

print(height(a))