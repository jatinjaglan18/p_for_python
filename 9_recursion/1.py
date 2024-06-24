#print increasing decreasing
n = int(input())
def dec(n):
    if n == 0:
        return
    print(n)
    dec(n-1)

#dec(n)

def inc(n):
    if n == 0:
        return 
    inc(n-1)
    print(n)

#inc(n)

def dec_inc(n):
    if n == 0:
        return
    print(n)
    dec_inc(n-1)
    print(n)

dec_inc(n)