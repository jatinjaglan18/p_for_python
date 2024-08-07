#Binary Tree

class Node:
    def __init__(self, data = None , left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
arr = [50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
def genrateTree(arr):
    stack = []
    root = Node(arr[0])
    stack.append([root, 1])

    idx = 0
    while stack:
        top = stack[-1]
        if top[1] == 1:
            idx += 1
            if arr[idx] != None:
                new_node = Node(arr[idx])
                top[0].left = new_node
                top[1] += 1
                stack.append([new_node,1])

            else:
                top[1] += 1
        elif top[1] == 2:
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

root = genrateTree(arr)
def display(node):
    if node == None:
        return 
    
    if node.left == None:
        l = '.'
    else:
        l = str(node.left.data)
    
    if node.right == None:
        r = '.'
    else:
        r = str(node.right.data)

    print(l + ' <-',node.data, '-> ' + r)
    display(node.left)
    display(node.right)

display(root)

#tilt of a binary tree
tilt = 0
def tilt_of_tree(node):
    global tilt
    if node == None:
        return 0

    l = tilt_of_tree(node.left)
    r = tilt_of_tree(node.right)
    s = l + r + node.data
    tilt += abs(l-r)
    return s 

#print(tilt_of_tree(root))
#print(tilt)

def isbinary(node):
    
    if node == None:
        return (True, float('inf'), float('-inf'))   #isbst,  minimum,  maximum

    lbst, lmin, lmax  = isbinary(node.left)
    rbst, rmin, rmax = isbinary(node.right)
    

    nmin = min(node.data,lmin,rmin)
    nmax = max(node.data,lmax,rmax)

    if lbst and rbst and node.data >= lmax and node.data <= rmin:
        return (True , nmin, nmax)
    else:
        return (False, nmin, nmax)
    
#isbst, min, max = isbinary(root)
#print(isbst)

#balanced Binary Tree
flag = True
def balanced(node):
    global flag
    if node == None:
        return -1

    lh = balanced(node.left)
    rh = balanced(node.right)

    ht = max(lh,rh) + 1
    if abs(lh-rh) > 1:
        flag = False
    return ht

def isbal(node):
    if node == None:
        return (True,-1)

    flag, lh = isbal(node.left)
    flag, rh = isbal(node.right)

    ht = max(lh,rh) + 1
    if abs(lh-rh) > 1:
        flag = False
    return flag, ht        

print(isbal(root)[0])
print(flag)
balanced(root)
