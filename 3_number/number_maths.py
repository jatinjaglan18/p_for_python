print('Addition of any base')

k = int(input('Base: '))
n1 = int(input('1st Number According to base: '))
n2 = int(input('2nd Number According to base: '))


def any_base_addition(n1, n2, k):
    c = 0
    num = 0
    m = 0
    while n1 > 0 or n2 > 0 or c > 0:
        a = n1 % 10
        b = n2 % 10
        d = a + b + c

        
        num = num + ((d % k) * (10**m))

        c = d // k


        m +=1
        n1 = n1 // 10
        n2 = n2 // 10

    return num
        
print(any_base_addition(n1,n2,k))

print('Subtraction of any base')

k = int(input('Base: '))
n1 = int(input('Greater Number According to base: '))
n2 = int(input('Smaller Number According to base: '))

def any_base_subtraction(n1,n2,k):
    m = 0
    c = 0
    num = 0
    while n1 > 0:
        a = n1 % 10
        b = n2 % 10

        d = 0
        a = a + c
        if a >= b:
            c = 0
            d = a - b

        else: 
            c = -1
            d = a + k - b

        num = num + (d * (10**m))
        n1 = n1 // 10
        n2 = n2 // 10
        m += 1
    return(num)
        
print(any_base_subtraction(n1,n2,k))


print('Multiplication of any base')

def mul_with_one(n,d,b):
    num = 0
    e = 0
    c = 0
    while n > 0 or c > 0:
        a = n % 10
        m = a * d
        m = m + c
        c = m // b
        p = m % b

        num = num + (p*(10**e))
        n = n // 10
        e += 1
    return num

def any_base_multiplication(n1,n2,b):
    num = 0
    m = 0
    while n2 > 0:
        d = n2 % 10
        val = mul_with_one(n1,d,b)
        val = val*(10**m)
        num = any_base_addition(num,val,b)

        n2 = n2 // 10
        m += 1

    return num

k = int(input('Base: '))
n1 = int(input('1st Number According to base: '))
n2 = int(input('2nd Number According to base: '))
print(any_base_multiplication(n1,n2,k))