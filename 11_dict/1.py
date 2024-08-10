#hashmap / dictionary

d = {}
d['India'] = 140
d['USA'] = 50
d['UK'] = 20
print(d.get('UK',0))
d['UK'] = 25
print('China' in d)
print('UK'in d)

print(d.items())
print(d.keys())
print(d.values())

for i in d.items():
    print(i)

for i in d.keys():
    print(i,d[i])

s = set(d.keys())
for i in s:
    print(i,d[i])

l = list(d.keys())
for i in range(len(l)):
    print(i,l[i],d[l[i]])
