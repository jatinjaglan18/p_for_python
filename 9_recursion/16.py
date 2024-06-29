#Knights Tour

n = int(input('Size: '))
chess = [[0 for i in range(n)] for i in range(n)]
r = int(input('Starting Row: '))
c = int(input('Starting Col: '))

def knightsTour(chess, sr, sc, move):
    if sr < 0 or sc < 0 or sr >= len(chess) or sc >= len(chess) or chess[sr][sc]  != 0:
        return
    elif move == len(chess) * len(chess):
        chess[sr][sc] = move
        displayBoard(chess)
        chess[sr][sc] = 0
        return
    
    
    chess[sr][sc] = move
    knightsTour(chess, sr - 2, sc + 1, move + 1)
    knightsTour(chess, sr - 1, sc + 2, move + 1)
    knightsTour(chess, sr + 1, sc + 2, move + 1)
    knightsTour(chess, sr + 2, sc + 1, move + 1)
    knightsTour(chess, sr + 2, sc - 1, move + 1)
    knightsTour(chess, sr + 1, sc - 2, move + 1)
    knightsTour(chess, sr - 1, sc - 2, move + 1)
    knightsTour(chess, sr - 2, sc - 1, move + 1)
    chess[sr][sc] = 0

def displayBoard(chess):
    for i in range(len(chess)):
        for j in range(len(chess)):
            print(chess[i][j], end = ' ')
        print()

knightsTour(chess, r, c, 1)