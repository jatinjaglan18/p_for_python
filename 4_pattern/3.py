'''
Code : Alpha Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 3
 A
 BB
 CCC
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 26

'''
k = chr(ord('A'))

n = int(input())

for i in range(1,n+1):
    for j in range(i):
        print(chr(ord('A')+i-1), end='')
    print()


'''
Code : Character Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 13

'''
for i in range(1,n+1):
    for j in range(i):
        print(chr(ord('A')+i+j-1), end='')
    print()


'''
Code : Interesting Alphabets

Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
Input format :
N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 26

'''

for i in range(1,n+1):
    for j in range(i):
        print(chr(ord('A')+n-i+j), end='')
    print()