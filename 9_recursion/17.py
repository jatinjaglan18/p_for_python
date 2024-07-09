#Taylor series
p = 1
f = 1
def e(x,n):
    global p, f
    if n == 0:
        return 1

    res = e(x,n-1)
    p = p * x
    f = f * n
    res = res + p/f
    return res

print(e(4,15))
n = 15
x = 4
s = 1
while n > 0:
    s = (1 + (x * s/ n))
    n -= 1

print(s)

s = 1
def ex(x,n):
    global s
    if n == 0:
        return s
    s = (1+(x*s/n))
    return ex(x,n-1)

print(ex(4,15))