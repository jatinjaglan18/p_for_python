#factorial
n = int(input())

def fac(n):
    if n == 1:
        return 1
    fnm1 = fac(n-1)
    res = n*fnm1
    return res
print(fac(n))