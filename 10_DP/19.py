#Tiling with 2 * 1 

#tiles -> length = 2 width = 1
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