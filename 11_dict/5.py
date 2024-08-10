#Longest consecutive subsquence

size = int(input())
arr = [int(input()) for i in range(size)]

d = {}
for i in arr:
    d[i] = True

#print(d)
for i in d.keys():
    if i - 1 in d.keys():
        d[i] = False

#print(d)

st = arr[0]
max_len = 0

for i in d.keys():
    if d[i]:
        temp = i
        tl = 1
        while temp + 1 in d.keys():
            tl += 1
            temp = temp + 1
        
        if max_len < tl:
            st = i
            max_len = tl 

for i in range(max_len):
    print(st + i)
