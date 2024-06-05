'''
Code : Star Pattern

Print the following pattern
Pattern for N = 4
...*
..*** 
.*****
*******
 
The dots represent spaces.

Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Constraints :
0 <= N <= 50

'''

n = int(input())

for row in range(1,n+1):
    for space in range(n-row):
        print(' ', end='')
    
    for star in range(2*row,1,-1):
        print('*', end ='')
    
    '''for s in range(2*row-2,row-1,-1):
        print('*', end='')'''
    print()
