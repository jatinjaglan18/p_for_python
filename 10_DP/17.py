#Paint house

n = int(input())
arr = [[int(input()) for i in range(3)] for j in range(n)]

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

print(paint_house(arr))