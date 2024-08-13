#Paint fence at most two with same color

f = int(input('No. of fence: '))
c = int(input('No. of colors: '))

def paint_fence(f,c):
    same = c        #last two fence are same
    diff = c*(c-1)  #last two fence are different
    total = same + diff

    for i in range(2,f):
        same = diff
        diff = total*(c-1)
        total = same + diff

    return total

print(paint_fence(f,c))