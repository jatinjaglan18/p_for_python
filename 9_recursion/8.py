#Stairs path
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