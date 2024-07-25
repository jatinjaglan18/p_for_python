#Generic Tree Multisolver

class Node:
    def __init__(self,value):
        self.data = value
        self.children = []
arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,150,-1,-1,-1]
sarr = [10,20,-1,30,50,-1,60,-1,-1,40,-1,-1]

def GenricTree(arr):
    
    root = Node(arr[0])
    stack = [root]
    for i in range(1,len(arr)):
        if arr[i] == -1:
            stack.pop()
        else:
            new_node = Node(arr[i])
            top = stack[-1]
            top.children.append(new_node)
            stack.append(new_node)

    return root

a = GenricTree(arr)

def display(root):
    string = str(root.data) + '->' 
    for i in range(len(root.children)):
        if i == len(root.children)-1:
            string = string + str(root.children[i].data)
        else:
            string = string + str(root.children[i].data) + ','
    print(string)
    for i in root.children:
        display(i)

display(a)

# size
# min value
# max value
# height
size = 0
min_val = float('inf')
max_val = float('-inf')
height = 0

def multisolver(node,depth):
    global size
    global min_val
    global max_val
    global height
    
    size += 1
    min_val = min(min_val,node.data)
    max_val = max(max_val,node.data)
    height = max(height,depth)
    
    for i in node.children:
        multisolver(i,depth+1)

multisolver(a,0)
'''print(size)
print(min_val)
print(max_val)
print(height)'''

pre = None
suc = None
state = 0
def pre_suc(node,data):
    global pre 
    global suc
    global state
    if state == 0:
        if node.data == data:
            state = 1
        else:
            pre = node.data
    elif state == 1:
        suc = node.data
        state = 2
    
    for i in node.children:
        pre_suc(i,data)

'''pre_suc(a,150)
print(pre)
print(suc)'''

ceil = float('inf')
floor = float('-inf')

def ceil_floor(node,data):
    global ceil
    global floor

    if node.data < data and node.data > floor:
        floor = node.data
        
    if node.data > data and node.data < ceil:
        ceil = node.data
    
    for i in node.children:
        ceil_floor(i,data)


'''ceil_floor(a,200)
print(ceil)
print(floor)'''

f = float('-inf')
def c_floor(node,data):
    global f
    if node.data > f and node.data < data:
        f = node.data
    for i in node.children:
        c_floor(i,data)

def kth_largest(node,k):
    global f
    res = float('inf')
    for i in range(k):
        c_floor(node,res)
        res = f
        f = float('-inf') 
    return res

print(kth_largest(a,3))
