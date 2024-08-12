#count binary string with no consecutive 0's
n = int(input())
def count_binary(n):
    b0 = 1      #count of strings ends with 0
    b1 = 1      #count of strings ends with 1

    for i in range(2,n+1):
        b_1 = b0 + b1
        b_0 = b1

        b0 = b_0
        b1 = b_1

    return b0+b1

print(count_binary(n))


#Arrange Buildings
#No buildings are consecutive

def arrange(n):
    b = 1
    s = 1

    #for one side of road
    for i in range(2,n+1):
        nb = s 
        ns = b + s

        b = nb
        s= ns
    
    bs1 = b + s
    #for both sides of road
    bs2 = bs1**2

    return bs2      #(b+s) ** 2

print(arrange(n))

    