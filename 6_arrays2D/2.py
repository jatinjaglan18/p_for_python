def matrix(n,m):
    mat = [[int(input()) for i in range(m)] for j in range(n)]
    return mat

n1 = int(input('Row1 '))
m1 = int(input('Col1 '))
matrix1 = matrix(n1,m1)

n2 = int(input('Row2 '))
m2 = int(input('Col2 '))
matrix2 = matrix(n2,m2)

def multiply(m1,m2):
    mat = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(len(m2)):
                mat[i][j] +=  m1[i][k] * m2[k][j] 

    return mat

if m1 != n2:
    print('Invalid Input')
else:
    print(multiply(matrix1,matrix2))
