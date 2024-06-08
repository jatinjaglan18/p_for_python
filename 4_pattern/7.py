n = int(input())
'''
*
**
***
****
*****
'''

for i in range(1,n+1):
    for j in range(i):
        print('*', end ='')

    print()

print()
'''
*****
*****
****
***
**
*
'''

for i in range(n, 0, -1):       #n
    for j in range(i):          #n-i
        print('*', end ='')

    print()

print()
'''
    *
   **
  ***
 ****
*****
'''

for i in range(1,n+1):
    for space in range(n-i):
        print(' ', end = '')
    for star in range(i):
        print('*', end = '')

    print()

print()
'''
*****
 ****
  ***
   **
    *
'''
for i in range(n):
    for space in range(i):
        print(' ', end = '')
    for star in range(n - i ):
        print('*', end = '')
    
    print()
'''
  *
 ***
*****
 ***
  *
'''
print()
sp = n // 2
st = 1

for row in range(n):
    for i in range(1, sp+1):
        print(' ', end = '')
    for j in range(1, st+1):
        print('*', end = '')
    
    if row < n // 2:
        sp -= 1
        st += 2
    else:
        sp += 1
        st -= 2
    print()