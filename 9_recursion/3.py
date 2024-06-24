#2 recursive calls
#Euler Path

def calls(n):
    if n == 0:
        return
    print('Pre' + str(n))
    calls(n-1)              #Left call
    print('In' + str(n))
    calls(n-1)              #Right call
    print('Post' + str(n))
calls(3)