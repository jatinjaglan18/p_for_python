#Get paths of maze

n = int(input('Size: '))
m = int(input('Size: '))

def mazePaths(sr,sc,dr,dc):
    if sr == dr and sc == dc:
        res=['']
        return res
    h = []
    v = []
    if sc < dc:
        h = mazePaths(sr,sc+1,dr,dc)
    if sr < dr:
        v = mazePaths(sr+1,sc,dr,dc)
    res = []
    for i in h:
        res.append('h' + i)
    for j in v:
        res.append('v' + j)

    return res

print(mazePaths(1,1,n,m))
