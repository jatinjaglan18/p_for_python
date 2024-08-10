#Highest frequency character
d = {}
s = input()

for i in s:
    d[i] = 1 + d.get(i,0)

    '''if i in d:
        d[i] += 1
    else:
        d[i] = 1'''

freq = d[s[0]]
ch = s[0]
for i in d.keys():
    if freq < d[i]:
        freq = d[i]
        ch = i
print(ch)