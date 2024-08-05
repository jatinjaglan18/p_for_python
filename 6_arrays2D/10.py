#Search in a Sorted 2D array
def matrix(n,m):
    mat = [[int(input()) for i in range(m)] for j in range(n)]
    return mat

n = int(input())
m = int(input())

mat = matrix(n,m)
print(mat)

f = int(input('Find: '))

i = 0
j = len(mat[0])-1

while i < len(mat) and j > -1:
    if f == mat[i][j]:
        print(i,j)
        break
    elif f < mat[i][j]:
        j -= 1
    else:
        print(i)
        i += 1
else:
    print('Not Found')
