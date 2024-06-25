#Tower of Hanoi
n = int(input('Number of Disks: '))
t1 = input('Origin of Disks: ')
t2 = input('Destination of Disks: ')
t3 = input('Used for moving disks: ')



def toh(n,t1,t2,t3,l):
    if n == 0:
        return
    toh(n-1,t1,t3,t2,l)
    print(n,'[' + t1 + ' -> ' + t2 +']')
    l.append(1)
    toh(n-1,t3,t2,t1,l)
    return len(l)
a = toh(n,t1,t2,t3,[])
print(a)