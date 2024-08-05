#Diagonal Traversal
def matrix(n,m):
    mat = [[int(input()) for i in range(m)] for j in range(n)]
    return mat

n = int(input())
m = int(input())

mat = matrix(n,m)
print(mat)

k = 0
while k < n:
    i = 0
    j = k

    while j < m :
        print(mat[i][j])
        i += 1
        j += 1
    
    k += 1