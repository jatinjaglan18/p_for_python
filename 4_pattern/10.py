'''
n = 5
..1
.232
34543
.232
..1
Dots repersent spaces
'''

n = int(input())

sp = n//2
st = 1
val = 1
for i in range(1,n+1):
    for space in range(sp):
        print(' ', end= '')

    v = val
    for star in range(st):

        print(v , end='')

        if star < st // 2:
            v += 1

        else:
            v -= 1

    if i < n//2 + 1:
        sp -= 1
        st += 2
        val += 1

    else:
        sp += 1
        st -= 2
        val -=1

    print()