'''
n = 4
1     1
12   21
123 321
1234321
'''

n = int(input())
sp = 2*n - 3
for i in range(1,n+1):
    for inc in range(1,i+1):
        print(inc, end = '')

    for space in range(sp):
        print(' ', end = '')
        
    if sp < 0:
        for dec in range(i,1,-1):
            print(dec-1, end='')

    else:
        for dec in range(i,0,-1):
            print(dec, end='')

    sp -= 2
    print()