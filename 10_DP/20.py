#Friends pairing problem

n = int(input('No. of friends: '))

def pairing(n):
    dp = [0 for i in range(n+1)]

    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1] + (i-1) * dp[i-2]
    
    return dp[n]

print(pairing(n))