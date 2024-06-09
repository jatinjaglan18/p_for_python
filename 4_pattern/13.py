'''
Star Hour Glass
n = 7
*******
 *   *
  * *
   *
  ***
 *****
*******
'''
n = int(input())

isp = n - 4
sp = 0
st = n
for i in range(n):
    if i > 0 and i < n // 2:
        for sapce in range(sp):
            print(' ', end = ' ')

        print('*', end = ' ')

        for space in range(isp):
            print(' ', end = ' ')

        print('*', end = ' ')
        isp -= 2

    else:

        for sapce in range(sp):
            print(' ', end = ' ')

        for star in range(st):
            print('*', end = ' ')
        
    if i < n // 2:
        sp += 1
        st -= 2
    else:
        sp -= 1
        st += 2

    print()
