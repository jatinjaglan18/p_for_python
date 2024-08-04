#2D array

n = int(input('No. of Rows: '))
m = int(input('No. of columns: '))

#matrix = [[int(input()) for j in range(m)] for i in range(n)]

#matrix = [[0 for i in range(m)] for i in range(n)]
matrix =[]
for i in range(n):
    print('Enter The Values for ' + str(i) + 'th row')
    next_row = []
    for j in range(m):
        next_row.append(int(input()))
        #matrix[i][j] = int(input())
    matrix.append(next_row)

#print(matrix)

for i in range(len(matrix)):
    
    for j in range(len(matrix[0])):
        print(matrix[i][j], end = ' ')
    print()