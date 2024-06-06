low = int(input())
high = int(input())

for i in range(low, high+1):
    if i == 1 or i == 2:
        print(i,end=' ')
    else:

        for j in range(2,int(i**0.5+1)):
            if i % j == 0:
                break
        else:
            print(i, end=' ')
