#Flood Fill
n = int(input('Rows: '))
m = int(input('Columns: '))

#arr = [[int(input('Give value of ' + str(j) + str(i) +' :')) for i in range(m)] for j in range(n)]
arr = [[int(i) for i in input().split()] for i in range(n)]

'''arr = [[0, 1, 0, 0, 0, 0, 0], 
[0, 1, 0, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 0, 0], 
[1, 0, 1, 1, 0, 1, 1], 
[1, 0, 1, 1, 0, 1, 1], 
[1, 0, 0, 0, 0, 0, 0]]'''

visited = [[0 for i in range(m)] for i in range(n)]

def floodFill(maze, sr, sc , dr, dc, paths, visit):
    if sr == dr and sc == dc:
        print(paths)
        return
    
    if maze[sr][sc] == 1 or visit[sr][sc] == 1:
        return
    
    visit[sr][sc] = 1
    #Top
    if sr > 0 :
        floodFill(maze, sr - 1 , sc , dr, dc, paths+'t',visit)
        
    #Left    
    if sc > 0 :
        floodFill(maze, sr , sc - 1 , dr, dc, paths+'l',visit)    

    #Down
    if sr < dr :
        floodFill(maze, sr + 1 , sc , dr, dc, paths+'d',visit)

    #Right
    if sc < dc :
        floodFill(maze, sr, sc + 1 , dr, dc, paths+'r',visit)

    visit[sr][sc] = 0

floodFill(arr,0,0,n-1,m-1,'', visited)