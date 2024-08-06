#stair paths
#Memoization
def countPaths(n,qb):
    if n == 0 :
        return 1
    elif n < 0:
        return 0
    if qb[n] > 0:
        return qb[n]
    print('hello',n)
    n1 = countPaths(n-1,qb)
    n2 = countPaths(n-2,qb)
    n3 = countPaths(n-3,qb)

    total = n1+n2+n3
    
    qb[n] = total
    return total
n = int(input())
qb = [0 for i in range(n+1)]
print(countPaths(n,qb))

#Tabulation
def countPathsTab(n):
    arr = [0 for i in range(n+1)]           #storage
    
    arr[0] = 1                              #Meaning

    for i in range(1, n+1, 1):              #Direction

        if i == 1:                          #Travel & Solve
            arr[i] = arr[i-1]
        elif i == 2 :
            arr[i] = arr[i-1] + arr[i-2]
        else:
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]    

    return arr[n]

print(countPathsTab(n))