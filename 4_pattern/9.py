n = int(input())

'''
n = 4
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
k = 1
for i in range(n):
    for j in range(i+1):
        print(k, end=' ')
        k+=1
    print()

'''
n = 5

0 
1 1 
2 3 5 
8 13 21 34 
55 89 144 233 377
'''
a = 0
b = 1
for i in range(n):
    for j in range(i+1):
        
        print(a, end=' ')
        c = a+b
        a = b
        b = c
    print()

'''
n = 5
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
for i in range(n):
    val = 1
    for j in range(i+1):   
        print(val, end=' ')
        val = (val * (i-j))//(j+1)  #use concepts of combination 

    print()

