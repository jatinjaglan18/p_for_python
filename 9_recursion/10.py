#get maze paths with jumps

n = int(input())
m = int(input())

def mazePathsjumps(sr,sc,dr,dc):
    if sr == dr and sc == dc:
        res = ['']
        return res
    l = []
    #Horizontal Moves
    if sc < dc:
        for js in range(1, dc):
            h = mazePathsjumps(sr,sc+js,dr,dc)
            for i in h:
                l.append('h'+ str(js) + i)

    #Vertical Moves
    if sr < dr:
        for js in range(1,dr):
            v = mazePathsjumps(sr+js,sc,dr,dc)
            for i in v:
                l.append('v' + str(js) + i)
    
    #Diagonal Moves 
    if sr < dr and sc < dc:
        for js in range(1,dr):
            d = mazePathsjumps(sr+js, sc+js , dr, dc)
            for i in d:
                l.append('d' + str(js) + i)
    return l

print(mazePathsjumps(1,1,n,m))