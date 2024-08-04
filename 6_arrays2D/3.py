def matrix(n,m):
    mat = [[int(input()) for i in range(m)] for j in range(n)]
    return mat

n = int(input())
m = int(input())

mat = matrix(n,m)
for j in range(len(mat[0])):
    if j % 2 == 0:
        for i in range(len(mat)):
            print(mat[i][j], end = ' ')

    else:
        for i in range(len(mat)-1,-1,-1):
            print(mat[i][j], end = ' ')
        
