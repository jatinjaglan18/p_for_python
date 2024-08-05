#Shell Rotate
def matrix(n,m):
    mat = [[int(input()) for i in range(m)] for j in range(n)]
    return mat

n = int(input())
m = int(input())

mat = matrix(n,m)
print(mat)

r = int(input('Rotations: '))
s = int(input('Shell No.: '))



def shell_to_1d(mat,sr,er,sc,ec):
    arr_1d = []

    i = sr
    j = sc

    while i <= er:
        arr_1d.append(mat[i][j])
        i += 1

    i -= 1
    j += 1

    while j <= ec:
        arr_1d.append(mat[i][j])
        j += 1

    j -= 1
    i -= 1

    while i >= sr:
        arr_1d.append(mat[i][j])
        i -= 1

    i += 1
    j-= 1

    while j > sc:
        arr_1d.append(mat[i][j])
        j -= 1

    return arr_1d

def rotate(arr,r):
    r = r % len(arr)
    if r < 0:
        r = len(arr) + r

    arr1 = arr[:len(arr) - r]
    arr2 = arr[len(arr) - r:]

    #arr1.reverse()
    #arr2.reverse()
    rev(arr1)
    rev(arr2)

    arr = arr1+arr2
    #arr.reverse()
    rev(arr)
    return arr

def rev(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] =  arr[len(arr)-i-1], arr[i]
    return arr

def oneD_to_shell(arr,mat,sr,er,sc,ec):
    i = sr
    j = sc
    idx = 0 
    while i <= er:
        mat[i][j] = arr[idx]
        i += 1
        idx += 1

    i -= 1
    j += 1

    while j <= ec:
        mat[i][j] = arr[idx]
        j += 1
        idx += 1
        
    j -= 1
    i -= 1

    while i >= sr:
        mat[i][j] = arr[idx]
        i -= 1
        idx += 1

    i += 1
    j-= 1

    while j > sc:
        mat[i][j] = arr[idx]
        j -= 1
        idx += 1

    return mat

def shell_rotate(mat,s,r):
    sr = s-1 
    er = len(mat) - s
    sc = s - 1
    ec = len(mat[0]) - s

    arr_1d = shell_to_1d(mat,sr,er,sc,ec)
    arr = rotate(arr_1d,r)
    mat = oneD_to_shell(arr,mat,sr,er,sc,ec)
    return mat
    
shell_rotate(mat,s,r)
print(mat)
