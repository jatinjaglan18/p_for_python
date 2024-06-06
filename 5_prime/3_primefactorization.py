i = int(input())

'''j = 2
while i > 1:
    if i % j == 0:
        print(j)
        i = i // j
    else:
        j += 1'''

#optimised
for k in range(2, int(i**0.5+1)):
    while i % k == 0:
        
        print(k)
        i = i // k


if i != 1 :
    print(i)