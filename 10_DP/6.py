#Goldmine
n = int(input())
m = int(input())
maze = [[int(input()) for i in range(m)] for j in range(n)]

def goldmine(maze,n,m):
    dp = [[0 for i in range(m)] for j in range(n)]

    for j in range(m-1,-1,-1):
        for i in range(n-1,-1,-1):
            if j == m-1:
                dp[i][j] = maze[i][j]

            elif i == n-1:
                dp[i][j] = maze[i][j] + max(dp[i][j+1],dp[i-1][j+1])
            
            elif i == 0:
                dp[i][j] = maze[i][j] + max(dp[i][j+1],dp[i+1][j+1])

            else:
                dp[i][j] = maze[i][j] + max(dp[i][j+1],dp[i-1][j+1],dp[i+1][j+1])

    gold = dp[0][0]
    for i in range(len(dp)):
        if dp[i][0] > gold:
            gold = dp[i][0]
    return gold

print(goldmine(maze,n,m))