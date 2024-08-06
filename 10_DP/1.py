#Fibonacci series using recursion
n = int(input())
def fib(n):
    if n == 0 or n == 1:
        return n
    
    print('hello', n)
    
    fibn1 = fib(n-1)
    fibn2 = fib(n-2)

    fibn = fibn1 + fibn2

    return fibn

print(fib(n))

#Dynamic Programming
#Memoization

def fib_Dp(n,qb):
    if n == 0 or n == 1:
        return n
    
    if qb[n] != 0 :
        return qb[n]
    
    print('hello', n)
    
    fibn1 = fib_Dp(n-1,qb)
    fibn2 = fib_Dp(n-2,qb)
    
    fibn = fibn1 + fibn2

    qb[n] = fibn
    return fibn

n = int(input())
qb = [0 for i in range(n+1)]
print(fib_Dp(n,qb))
print(qb)