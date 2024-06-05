'''
Code : Triangle of Numbers

Print the following pattern for the given number of rows.
Pattern for N = 4
...1
..232
.34543
4567654
The dots represent spaces.

Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50

'''

n = int(input())

for row in range(1,n+1):
    i=0
    for space in range(n-row):
        print(' ', end='')
    
    for inc in range(n-row,n):        
        print(row+i, end = '')
        i+=1

    for dec in range(2*row-2,row-1,-1):
        print(dec, end = '')
    print()