#Celebrity Problem
n = int(input())

#a = [[int(input()) for i in range(n)] for i in range(n)]
matrix = []
for i in range(n):
    print('Provide Values of row', i)
    row = [int(input()) for i in range(n)]
    matrix.append(row)
print(matrix)

#Most Probably o(n)
celebs = None
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            break
    else: 
        celebs = i
        break
else:
    print(celebs)

if celebs != None:
    for i in range(n):
        if i != celebs:
            if matrix[i][celebs] == 0:
                celebs = None
                break
    print(celebs)


#Alternate o(n)
stack = []
for i in range(n):
    stack.append(i)

while len(stack) >= 2:
    a1 = stack.pop()
    a2 = stack.pop()

    if matrix[a1][a2] == 1:
        stack.append(a2)
    else:
        stack.append(a1)

celebs = stack.pop()

for i in range(n):
    if i != celebs:
        if matrix[i][celebs] == 0 or matrix[celebs][i] == 1:
            print(None)
            break
else:
    print(celebs)

