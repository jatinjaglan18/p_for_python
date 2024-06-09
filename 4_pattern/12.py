'''
n = 5
..*
..**
*****
..**
..*

Dots repersent spaces
'''
n = int(input())
st = 1
for i in range(n):
    if i == n // 2  :
        for j in range(n):
            print('*' , end = '')

    else:
        for space in range(n//2):
            print(' ', end = '')
        for star in range(st):
            print('*', end ='')

    if i < n // 2:
        st+=1
    else:
        st -= 1
    print()

print()

#Alternate
st = 1
for i in range(n):

    for space in range(n//2):
        if i == n // 2  :
            print('*' , end = '')
        else:   
            print(' ', end = '')

    for star in range(st):
        print('*', end ='')

    if i < n // 2:
        st+=1
    else:
        st -= 1
    print()