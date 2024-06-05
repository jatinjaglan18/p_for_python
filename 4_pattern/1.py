'''
Code : Square Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 4
4444
4444
4444
4444

Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50

'''


i = int(input())

for row in range(i):
    for col in range(i):
        print(i, end='')
    print()


'''
Code : Triangular Star Pattern

Print the following pattern for the given N number of rows.
Pattern for N = 4
*
**
***
****

Note : There are no spaces between the stars (*).
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50

'''
j = int(input())

for row in range(1,j+1):
    for col in range(row):
        print(row, end='')

    print()


#Code : Triangle Number Pattern