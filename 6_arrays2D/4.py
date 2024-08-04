#Spiral
def matrix(n,m):
    mat = [[int(input()) for i in range(m)] for j in range(n)]
    return mat

n = int(input())
m = int(input())

mat = matrix(n,m)
print(mat)
top = 0
bottom = len(mat)
left = 0
right = len(mat[0])

#i = 0
dir = 0
while top <= bottom and left <= right: #i < n*m:
    if dir == 0:
        for j in range(top,bottom,1):
            print(mat[j][left],end = ' ')
        left += 1
    
    elif dir == 1:
        for j in range(left, right,1):
            print(mat[bottom-1][j],end=' ')
        bottom -= 1

    elif dir == 2:
        for j in range(bottom-1,top-1,-1):
            print(mat[j][right-1],end=' ')
        right -= 1
    
    elif dir == 3:
        for j in range(right-1,left-1,-1):
            print(mat[top][j],end=' ')
        top += 1

    dir = (dir+1) % 4
    #i += 1 