#Minimum Cost Path using recursion
n = int(input())
m = int(input())
maze = [[int(input()) for i in range(m)] for j in range(n)]

cost = float('inf')
def min_cost(maze, sr,sc,dr,dc,c,path):
    global cost
    if sr == dr and sc == dc:
        c += maze[sr][sc]
        #print(path,c)
        if c < cost:
            cost = c

    if sc < dc:
        min_cost(maze,sr, sc+1, dr, dc, c + maze[sr][sc],path+'h')
    if sr < dr :
        min_cost(maze,sr+1, sc, dr, dc, c + maze[sr][sc],path+'v')

    
min_cost(maze,0,0,n-1,m-1,0,'')
print(cost)

#Dynamic Programming

def min_cost(maze, n, m):
    dp = [[0 for i in range(m)] for j in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:       #Destination
                dp[i][j] = maze[i][j]

            elif i == n-1:                  #Destination Row
                dp[i][j] = maze[i][j] + dp[i][j+1]
            elif j == m-1:                  #Destination Column
                dp[i][j] = maze[i][j] + dp[i+1][j]
            
            else:                           #ROM -> Rest of Maze
                dp[i][j] = maze[i][j] + min(dp[i][j+1],dp[i+1][j])

    return dp[0][0]

print(min_cost(maze,n,m))
