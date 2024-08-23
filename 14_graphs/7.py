#count number of islands

n = int(input())
m = int(input())

mat = [[int(i) for i in input().split()] for i in range(n)]

visited = [[False for j in range(m)] for i in range(n)]

def count_islands(mat,v):
    count = 0 
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0 and v[i][j] == False:
                tree(mat,i,j,v)
                count+=1
    return count

def tree(m,sr,sc,v):
    if sr < 0 or sc < 0 or sr >= len(m) or sc >= len(m[0]) or m[sr][sc] == 1 or v[sr][sc] == True:
        return

    v[sr][sc] = True
    #north
    tree(m,sr-1,sc,v)
    #east
    tree(m,sr,sc+1,v)
    #south
    tree(m,sr+1,sc,v)
    #west
    tree(m,sr,sc-1,v)

print(count_islands(mat,visited))