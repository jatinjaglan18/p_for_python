#Factorial
n = int(input())

def fac(n):
    if n == 1:
        return 1
    fnm1 = fac(n-1)
    res = n*fnm1
    return res
print(fac(n))

#Linear Power
def linear_power(x,n):
    if n == 0:
        return 1
    p = linear_power(x,n-1)
    res = x * p
    return res
x = int(input())
n = int(input())
print(linear_power(x,n))

def log_power(x,n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = log_power(x,n//2)
        res = half*half
        return res
    else:
        half = log_power(x,n//2)
        res = half*half*x
        return res
print(log_power(x,n))
