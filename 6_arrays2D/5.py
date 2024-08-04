#Exit point
def matrix(n,m):
    mat = [[int(input()) for i in range(m)] for j in range(n)]
    return mat

n = int(input())
m = int(input())

mat = matrix(n,m)
print(mat)

i = 0
j = 0
dir = 0
while True:
    dir = (dir + mat[i][j]) % 4
    if dir == 0:
        j += 1
    elif dir == 1:
        i += 1
    elif dir == 2:
        j -= 1
    elif dir == 3:
        i -= 1

    if i < 0:
        i += 1
        break

    elif j < 0:
        j += 1
        break

    elif i == len(mat):
        i -= 1
        break

    elif j == len(mat[0]):
        j -= 1
        break

print(i,j)

        
