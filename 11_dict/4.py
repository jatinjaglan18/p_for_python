#Get common elements 2 in two arrays
s1 = int(input())
a1 = [int(input()) for i in range(s1)]

s2 = int(input())
a2 = [int(input()) for i in range(s2)]

d1 = {}
for i in a1:
    d1[i] = 1 + d1.get(i,0)

for i in a2:
    if i in d1.keys() and d1[i] > 0 :
        print(i, end = ' ')
        d1[i] -= 1
        
        '''if d1[i] == 0:
            d1.pop(i)'''

