n = int(input())

def fac(n):

    fac = 1
    for i in range(1,n+1):
        fac *= i

    return fac


count = 0

fact = fac(n)
f = fact % 10

# Trailing Zeros
while f == 0:
    count += 1
    fact = fact // 10
    f = fact  % 10

print(count)

r = int(input())
