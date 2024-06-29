#N-Queens Problem Backtracking

n = int(input())
chess = [[0 for i in range(n)] for i in range(n)]
print(chess)

def printNQueens(chess, queens, row):
    if row == len(chess):
        print(queens)
        return

    for col in range(n):
        if safe_for_Queen(chess, row, col) :
            chess[row][col] = 1
            printNQueens(chess, queens + str(row) + str(col) + ' ', row + 1)
            chess[row][col] = 0 


def safe_for_Queen(chess, row, col):
    #vertical
    for i in range(row-1, -1, -1):
        if chess[i][col] == 1:
            return False

    #Daigonal 1
    i = row-1
    j = col-1
    while i >= 0 and j >= 0 :
        if chess[i][j] == 1:    
            return False
        i -= 1
        j -= 1

    #Daigonal 2
    i = row - 1
    j = col + 1
    while i >= 0 and j != len(chess):
        if chess[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

printNQueens(chess,'',0)