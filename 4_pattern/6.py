'''
Code : Diamond of stars

Print the following pattern for the given number of rows.
Note: N is always odd.

Pattern for N = 5
..*
.***
*****
.***
..*
 
The dots represent spaces.

Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49

'''

n = int(input())
u_p = (n//2) + 1
b_p = n - u_p

for u in range(u_p):

    for space in range(1,u_p-u):
        print(' ', end='')

    for star in range(2*u,-1,-1 ):
        print('*', end='')
    print()

for b in range(1,b_p+1):

    for space in range(b):
        print(' ', end='')

    for star in range(n-2*b):
        print('*', end='')
    print()
