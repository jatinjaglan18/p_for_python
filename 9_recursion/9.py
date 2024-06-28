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


#Print paths of maze

def print_maze_paths(sr,sc,dr,dc,path):
    #Call Smart, Base Case Normal
    if sr == dr and sc == dc:
        print(path)
        return 
    
    if sr < dr:         #Jis rashte jana nhi uska pta hi kyu lagana
        print_maze_paths(sr+1, sc , dr,dc,path + 'h')
    if sc < dc :
        print_maze_paths(sr,sc+1 ,dr,dc,path + 'v')

print_maze_paths(1,1,n,m,'')


def print_maze_paths(sr,sc,dr,dc,path):
    #Call Stupid, Base Case Normal
    if sr > dr or sc > dc:      #rashte ka pta h pr jana nhi h us rashte 
        return
    if sr == dr and sc == dc:
        print(path)
        return 
    print_maze_paths(sr+1, sc , dr,dc,path + 'h')
    print_maze_paths(sr,sc+1 ,dr,dc,path + 'v')

print_maze_paths(1,1,n,m,'')