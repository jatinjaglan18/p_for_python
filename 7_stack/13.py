#Merge Overlapping
n = int(input())

matrix = []
for i in range(n):
    print('Give st, et time for row:', i)
    a = input().split()
    n_r = []
    for j in a:
        n_r.append(int(j))
    matrix.append(n_r)

# Sort According to 1st element of 2D List
matrix = sorted(matrix, key = lambda x : x[0])

stack = []
stack.append(matrix[0])
for i in range(1,len(matrix)):
    val = matrix[i]

    if val[0] < stack[-1][1]:
        if val[1] > stack[-1][1]:
            stack[-1][1] = val[1]

    else:
        stack.append(val)

for i in stack:
    print(i)