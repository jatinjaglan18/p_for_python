'''
Code : Reverse Number Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 4
1
21
321
4321
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 

'''

n = int(input())

for i in range(1,n+1):
    for j in range(i):
        print(i-j, end='')
    print()


'''
Code : Inverted Number Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 4
4444
333
22
1
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50

'''

m = int(input())
for i in range(m):
    for j in range(m-i,0,-1):
        print(m-i, end='')
    print()

'''
Code : Mirror Number Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 4
...1 
..12
.123
1234
The dots represent spaces.

Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50

'''

n = int(input())

for row in range(1,n+1):
    i=0
    for space in range(n-row):
        print('.', end='')

    for col in range(n-row,n):
        i+=1
        print(i , end='')

    print()

