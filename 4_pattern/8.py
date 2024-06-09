'''
n = 5
***.***
**...**
*.....*
**...**
***.***

Dots Repersent spaces
'''
n = int(input())

st = n // 2 + 1
sp = 1

for i in range(1, n+1):
    for star in range(st):
        print('*', end='')
    for space in range(sp):
        print(' ', end= '')
    for s in range(st):
        print('*', end='')
    
    if i < n//2 +1:
        st -= 1
        sp += 2
    else:
        st += 1
        sp -= 2

    print()


'''
n = 5
*
.*
..*
...*
....*

Dots Repersent spaces
'''

for i in range(1, n+1):
    for space in range(1, i):
        print(' ', end='')
    for star in range(1):
        print('*', end= '')

    print()

#Alternate
for i in range(1,n+1):
    for space in range(1,i+1):
        if i == space:
            print('*', end ='')
        else:

            print(' ', end='')
    print()

'''
n = 5
....*
...*
..*
.*
*

Dots Repersent spaces
'''
for i in range(n):
    for j in range(5,i,-1):
        if j - 1 == i :
            print('*', end ='')
        else: 
            print(' ', end = '')
    print()

#Alternate
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j == n+1 :
            print('*', end='')
        else:
            print(' ', end='')
    print()    


'''
n = 5
*...*
.*.*
..*
.*.*
*...*

Dots Repersent spaces
'''
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j == n+1 or i == j :
            print('*', end='')
        else:
            print(' ', end='')
    print()    

'''
n = 5
..*
.*.*
*...*
.*.*
..*

Dots Repersent spaces
'''

o_sp = n // 2
i_sp = -1


for i in range(n):
    for o_s in range(o_sp):
        print(' ', end='')

    print('*', end='')

    for i_s in range(i_sp):
        print(' ', end ='')

    
    if i != 0 and i != n-1:  
        print('*', end='')

    if i < n// 2:
        o_sp -= 1
        i_sp += 2
    else:
        o_sp += 1
        i_sp -= 2
    print()