#Climb Stairs using Tabulation
n = int(input())
arr = [int(input()) for i in range(n)]

def countPaths(n,arr):
    dp = [0 for i in range(n+1)]
    dp[n] = 1

    for i in range(n-1,-1,-1):
        for j in range(1,arr[i]+1):
            if i + j <= n:
                dp[i] += dp[i+j]
        
    return dp[0]

print(countPaths(n,arr))
