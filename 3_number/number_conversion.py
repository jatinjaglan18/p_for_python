n = int(input('Number: '))
k = int(input('Base: '))

print('decimal_to_any_base')
def decimal_to_any_base(n,k):
    c_num = 0
    m = 0
    while n > 0:
        num = n % k
        c_num = num * (10 ** m) + c_num
        m += 1
        n = n // k

    return c_num

print(decimal_to_any_base(n,k))

print('any_base_to_decimal')
def any_base_to_decimal(n,k):
    m = 0
    c_num = 0
    while n > 0:
        num = n % 10
        c_num = c_num + num * (k ** m)
        m += 1
        n = n // 10

    return c_num

print(any_base_to_decimal(n,k))

print('any_base_to_any_base')
def any_base_to_any_base(n,k,j):
    num = any_base_to_decimal(n,k)
    c_num = decimal_to_any_base(num,j)
    return(c_num)

j = int(input('Base: '))
print(any_base_to_any_base(n,k,j))

