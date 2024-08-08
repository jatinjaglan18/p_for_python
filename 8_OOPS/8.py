#Binary Search Tree
class Node:
    def __init__(self, data = None , left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
arr = [12, 25, 37, 50, 62, 75, 87]
def genrateTree(arr,l,h):

    if l > h:
        return None
    
    mid = (l + h) // 2
    
    val = arr[mid]
    lc = genrateTree(arr,l,mid-1)
    rc = genrateTree(arr,mid+1,h)

    root = Node(val, lc, rc)
    return root

root = genrateTree(arr,0,len(arr)-1)
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

#size
def size(node):
    if node == None:
        return 0

    ls = size(node.left)
    rs = size(node.right)
    s = ls + rs + 1
    return s  

print(size(root))

#sum
def sum_bst(node):
    if node == None:
        return 0
    lc = sum_bst(node.left)
    rc = sum_bst(node.right)

    s = lc+rc+node.data
    return s

print(sum_bst(root))

#max of bst
def max_bst(node):
    if node.right == None:
        return node.data
    return max_bst(node.right)

print(max_bst(root))

#min of bst
def min_bst(node):
    if node.left == None:
        return node.data
    return min_bst(node.left)

print(min_bst(root))

#find
def find_bst(node,x):
    if node == None:
        return False
    if x < node.data:
        return find_bst(node.left,x)
    elif x > node.data:
        return find_bst(node.right,x)
    else:
        return True

print(find_bst(root,25))









'''ef isbinary(node):
    
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

#print(isbal(root)[0])
#print(flag)
#balanced(root)

n = None
size = 0
def largestBST(node):
    global n
    global size
    if node == None:
        return (True, float('inf'), float('-inf'), 0)
    
    isbstl, lmin, lmax, ls =largestBST(node.left)
    isbstr, rmin, rmax, rs = largestBST(node.right)

    ns = ls + rs + 1
    nmin = min(node.data,lmin,rmin)
    nmax = max(node.data,lmax,rmax)

    if isbstl and isbstr and node.data >= lmax and node.data <= rmin:
        if size < ns:
            size = ns
            n = node.data

        return (True, nmin, nmax, ns)
    else:
        return (False, nmin, nmax, ns)

largestBST(root)
print(n,'@',size)'''