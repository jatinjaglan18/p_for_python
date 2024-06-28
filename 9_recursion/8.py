#Get Stairs paths
n = int(input())

def getPaths(n):
    if n == 0:
        res = ['']
        return res
    elif n < 0:
        res = []
        return res
    
    f1 = getPaths(n-1)
    f2 = getPaths(n-2)
    f3 = getPaths(n-3)

    res = []
    for i in f1:
        res.append('1' + i)
    for i in f2:
        res.append('2' + i)
    for i in f3:
        res.append('3' + i)
        
    return res

print(getPaths(n))

#Print stair Paths
def print_stair_paths(n,path):
    if n == 0:
        print(path)
        return
    elif n < 0 :
        return
    
    for i in range(1,4):
        print_stair_paths(n-i, path + str(i))

print_stair_paths(n,'')