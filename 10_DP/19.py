#Tiling with 2 * 1 

#tiles -> length = 1 width = 2
length = int(input('length of floor: '))
#width of floor = 2

def tiling(l):
    dp = [0 for i in range(l+1)]

    dp[1] = 1
    dp[2] = 2

    for i in range(3,l+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[l])
    
    #fibonacci
    if l == 1:
        return 1
    elif l == 2:
        return 2
    else:
        a = 1
        b = 2
        for i in range(3,l+1):
            temp = a
            a = b 
            b += temp
        return b


print(tiling(length))


#Tiling m * n floor with m * 1

#tile -> length = 1
w = int(input('Width tile / floor: '))
l = int(input('Length of floor: '))

def tiling1(w,l):
    dp = [0 for i in range(l+1)]

    for i in range(1,l+1):
        if i < w:
            dp[i] = 1
        elif i == w:
            dp[i] = 2

        else:
            dp[i] = dp[i-1] + dp[i-w]
        
    return dp[l]

print(tiling1(w,l))