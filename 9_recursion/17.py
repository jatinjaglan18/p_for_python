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