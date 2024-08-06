#Minimum steps to Climb Stairs using Tabulation
n = int(input())
arr = [int(input()) for i in range(n)]

def minJumps(n,arr):
    dp = [float('inf') for i in range(n+1)]
    dp[n] = 0

    for i in range(n-1,-1,-1):
        for j in range(1,arr[i]+1):
            if i + j <= n:
                if dp[i] > dp[i+j]:
                    dp[i] = dp[i+j] + 1
    
    if dp[0] == float('inf'):
        return None
    
    return dp[0]

print(minJumps(n,arr))
