#Paint house with 3 colours

#n = int(input())
#arr = [[int(input()) for i in range(3)] for j in range(n)]

def paint_house(arr):
    red = arr[0][0]
    blue = arr[0][1]
    green = arr[0][2]

    for i in range(1,len(arr)):
        nred = arr[i][0] + min(blue,green)
        nblue = arr[i][1] + min(red,green)
        ngreen = arr[i][2] + min(red,blue)

        red = nred
        blue = nblue
        green = ngreen

    return min(red,blue,green)

#print(paint_house(arr))

#Paint houses with n numbers of colours
h = int(input('No. of houses: '))
c = int(input('No. of colors: '))

arr = [[int(input()) for colors in range(c)] for house in range(h)]

#o(n^3)
def paint_houses_n_colors(arr,h,c):
    dp = [[0 for colors in range(c)] for houses in range(h)]
    
    for j in range(c):
        dp[0][j] = arr[0][j]

    for i in range(1,len(dp)):
        for j in range(len(dp[0])):
            val = float('inf')
            for k in range(len(dp[0])):
                if k != j and dp[i-1][k] < val:
                    val = dp[i-1][k]

            dp[i][j] = arr[i][j] + val

    return min(dp[-1])

#print(paint_houses_n_colors(arr,h,c))

#o(n^2)
def paint_houses_n_colors(arr,h,c):
    dp = [[0 for colors in range(c)] for houses in range(h)]
    
    min_1 = float('inf')
    min_2 = float('inf')
    for j in range(c):
        dp[0][j] = arr[0][j]
        if arr[0][j] < min_1:
            min_2 = min_1
            min_1 = arr[0][j]
        elif arr[0][j] < min_2:
            min_2 = arr[0][j]

    for i in range(1,len(dp)):
        nmin_1 = float('inf')
        nmin_2 = float('inf')
        for j in range(len(dp[0])):
            
            if dp[i-1][j] == min_1:
                dp[i][j] = arr[i][j] + min_2
            else:
                dp[i][j] = arr[i][j] + min_1
                
            if dp[i][j] < nmin_1:
                nmin_2 = nmin_1
                nmin_1 = dp[i][j]
            elif dp[i][j] < nmin_2:
                nmin_2 = dp[i][j]
            
        min_1 = nmin_1
        min_2 = nmin_2

    return min_1

print(paint_houses_n_colors(arr,h,c))