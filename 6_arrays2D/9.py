#Saddle Point 
def matrix(n,m):
    mat = [[int(input()) for i in range(m)] for j in range(n)]
    return mat

n = int(input())
m = int(input())

mat = matrix(n,m)
print(mat)

for i in range(len(mat)):
    min_val = float('inf')
    k = 0
    l = 0 
    for j in range(len(mat[0])):
        if mat[i][j] < min_val :
            min_val = mat[i][j]
            k = i
            l = j
    
    for row in range(len(mat)):
        if min_val < mat[row][l]:
            flag = False
            break
    else:
        print('Value is:', min_val, 'at ', k, l)
        break
    
else:
    print('Invalid Input')
