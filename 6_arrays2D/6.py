#Rotate by 90
def matrix(n,m):
    mat = [[int(input()) for i in range(m)] for j in range(n)]
    return mat

n = int(input())
m = int(input())

mat = matrix(n,m)
print(mat)

#transpose
for i in range(len(mat)):
    for j in range(i,len(mat[0]),1):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

#Rotate by 90
for i in mat:
    #i.reverse()
    for j in range(len(i)//2):
        i[j],i[len(i)-1-j] = i[len(i)-1-j],i[j] 

print(mat)