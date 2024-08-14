#partiton into subsets

n = int(input('number: '))
k = int(input('team: '))

def partition(n,k):
    dp = [[0 for i in range(n+1)] for i in range(k+1)]

    for i in range(1,k+1):
        for j in range(1,n+1):
            if i > j:
                dp[i][j] == 0
            elif i == j or i == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + (dp[i][j-1] * i)

    return dp[k][n]

print(partition(n,k))