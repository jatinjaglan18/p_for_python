#Get common elements in two arrays
s1 = int(input())
a1 = [int(input()) for i in range(s1)]

s2 = int(input())
a2 = [int(input()) for i in range(s2)]

d1 = {}
for i in a1:
    d1[i] = 1 + d1.get(i,0)

'''d2 = {}
for i in a2:
    d2[i] = 1 + d2.get(i,0)'''

for i in a2:
    if i in d1.keys():
        print(i, end = ' ')
        d1.pop(i)
