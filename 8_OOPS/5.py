#Generic Tree

class Node:
    def __init__(self,val):
        self.data = val
        self.children = []
    
arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,150,-1,-1,-1]

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

    display(root)

def display(node):
    string = str(node.data) + '-->' 
    for i in node.children:
        string = string + ', ' + str(i.data)
    string = string + '.'
    print(string)
    for i in node.children:
        display(i)  

genrateTree(arr)